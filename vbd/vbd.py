import pandas as pd
import numpy as np

class VBD:
    def __init__(self, league_size, team_size, file):
        draft_size = league_size * team_size
        all_projections = pd.read_csv(file)

        # remove free agents and defense
        all_projections = all_projections.query("team != 'FA' and position != 'DB' and position != 'DL' and position != 'LB'")

        all_projections = all_projections.sort_values(by='overallRank')
        projections = all_projections.head(draft_size)

        all_positions = ['QB', 'RB', 'WR', 'TE', 'DST', 'K']

        replacements = {}

        for pos in all_positions:
            # Query the position players to find the last ranked at that position
            # that would be drafted
            expression = "position == '" + pos + "'"
            draft_pos = projections.query(expression)

            # Get the last rank in the draft
            draft_pos = draft_pos.sort_values(by='positionRank')
            last_rank = draft_pos.tail(1)['positionRank'].iloc[0]

            # Special case for defenses
            if last_rank != 32 and pos != 'DST':
                expression_2 = "positionRank > " + str(last_rank)

                # Get players by position
                replacement_players = all_projections.query(expression)

                # Get players and sort by rank
                replacement_players = replacement_players.query(expression_2)
                replacement_players = replacement_players.sort_values(
                    by='positionRank')

                # Get the projected points of the first replacement player
                replacement_points = replacement_players.head(1)['points'].iloc[0]
            else:
                replacement_points = draft_pos.tail(1)['points'].iloc[0]

            replacements[pos] = replacement_points

        # Extract only the relevant columns
        projections = projections[["player", "position", "team", "adp", "points"]]

        projections["vbd"] = 0
        projections = projections.apply(
            func=self.set_vbd_, axis=1, args=(replacements,), result_type='broadcast')
        projections = projections.sort_values(by="vbd", ascending=False)

        # Calculate the points above average for vbd
        averages = {
            "QB" : np.mean(projections.query("position == 'QB'")['vbd']),
            "RB" : np.mean(projections.query("position == 'RB'")['vbd']),
            "WR" : np.mean(projections.query("position == 'WR'")['vbd']),
            "TE" : np.mean(projections.query("position == 'TE'")['vbd']),
            "DST" : np.mean(projections.query("position == 'DST'")['vbd']),
            "K" : np.mean(projections.query("position == 'QB'")['vbd'])
        }

        projections["paa"] = 0
        projections = projections.apply(
            func=self.set_paa_, axis=1, args=(averages,), result_type='broadcast')

        self.projections = projections

    def draft(self, position):
        """Best to player to draft at given position
        :param str position: The position to draft. [QB, RB, WR, TE, DST, K, ANY]
        :return: a pandas DataFrame with one row
        """
        position = position.upper()
        if position == "ANY":
            return self.top(1, "ALL")
        else:
            return self.top(1, position)

    def remove(self, player):
        """Removes a player
        :param str player: The name of the player as it appears in the data
        :return: None
        """
        expression = "player != '" + player + "'"
        self.projections.query(expr=expression, inplace=True)

    def adjust(self, position, multiplier):
        """Adjust the VBD value of a certain position
        :param str position: The position to modify. [QB, RB, WR, TE, DST, K]
        :param float multiplier: The amount the multiply the VBD values by
        :return: None
        """
        self.projections = self.projections.apply(func=self.adjust_, axis=1, args=(position, multiplier), result_type="broadcast")
        self.projections.sort_values(by="vbd", inplace=True, ascending=False)

    def search(self, player):
        """Search for a player
        :param str player: The name of the player to search for
        :return: a pandas Dataframe
        """
        expression = "player == '" + player + "'"
        return self.projections.query(expression)

    def top(self, num, position):
        """Get the top n players of a position
        :param int num: The cutoff from the top
        :param str position: The desired position. [QB, RB, WR, TE, DST, K, ALL]
        :return: a pandas DataFrame
        """
        position = position.upper()
        if position == "ALL":
            top_players = self.projections.head(num)
        else:
            expression = "position == '" + position + "'"
            top_players = self.projections.query(expression).head(num)
        return top_players

    def load(self, file):
        """Load a file
        :param str file: The filename to load
        :return: None
        """
        self.projections = pd.read_csv(file)

    def save(self, file):
        """Save to a file
        :param str file: The file to save to
        :return: None
        """
        self.projections.to_csv(file, index=False)

    def set_vbd_(self, row, replacements):
        row["vbd"] = row["points"] - replacements[row["position"]]
        return row

    def set_paa_(self, row, averages):
        row["paa"] = row["vbd"] - averages[row["position"]]
        return row

    def adjust_(self, row, position, muliplier):
        if row["position"] == position:
            row["vbd"] *= multiplier
        return row
