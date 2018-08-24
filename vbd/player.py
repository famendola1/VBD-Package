class Player:
    def __init__(self, row):
        self.name = row["player"]
        self.position = row["position"]
        self.team = row["team"]
        self.adp = row["adp"]
        self.points = row["points"]
        self.vbd = row["vbd"]
        self.paa = row["paa"]

    def __repr__(self):
        print("Name: ", self.name)
        print("Position: ", self.position)
        print("Team: ", self.team)
        print("ADP: ", self.adp)
        print("Points: ", self.points)
        print("VBD: ", self.vbd)
        print("Points Above Average: ", self.paa)
