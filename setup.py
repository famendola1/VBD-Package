import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vbd",
    version="0.0.1",
    author="Fabio Amendola",
    author_email="fabio.amendola20@gmail.com",
    description="A package for value based drafting",
    scripts=["bin/fantasy-draft"]
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/famendola1/VBD-Package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
