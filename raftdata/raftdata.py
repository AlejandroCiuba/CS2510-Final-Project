# Get the Raft implementation information from the Raft website
import re

import pandas as pd


WEBSITE = "https://raft.github.io"
TABLE_ID = "implementations"

# 04/10/2024 at some time
PATH = "repos.html"
STARS = re.compile(r'([0-9,]+)')

def stars(x):

    if x is pd.NA:
        return 0
    elif isinstance(x, float):
        return x
    
    return float(x)

def main():

    raft_df = pd.read_html(PATH)[0]

    raft_df["Stars"] = raft_df["Stars"].map(stars)

    print(raft_df.info())
    print(raft_df.head(10))

    raft_df.to_csv("raft.csv", index=False, header=True)


if __name__ == "__main__":
    main()