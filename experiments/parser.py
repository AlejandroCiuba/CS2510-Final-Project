# Parse the results from a file
import argparse
import datetime
import re

import pandas as pd

PATH = "results"
SAVE = "results_csv"

RESULTS = re.compile(r'\bRESULT\b')

# Results should be stored in the same order per run across all implementations
FRAME = {"IMPLEMENTATION": [],
         "RUN_IN_FILE": [],
         "MESSAGES_SENT": [],
         "COMMIT_TIME": [],
         "CPU_UTIL": [],
         "MAX_MEM": [],
         "LOG_SIZE":[], }

def main(args: argparse.Namespace):

    RUN = 1

    with open(f"{PATH}/{args.file}", "r") as src:
        lines = src.readlines()

    for line in lines:

        if RESULTS.search(line):

            if "MESSAGES" in line:
                FRAME["MESSAGES_SENT"].append(int(line.split()[-1]))
            
            elif "COMMIT" in line:
                FRAME["COMMIT_TIME"].append(float(line.split()[-1]))

            elif "CPU" in line:
                FRAME["CPU_UTIL"].append(float(line.split()[-1][:-1]))

            elif "MEM" in line:
                FRAME["MAX_MEM"].append(float(line.split()[-2]))

            elif "LOG" in line:

                FRAME["IMPLEMENTATION"].append(args.implementation)
                FRAME["RUN_IN_FILE"].append(RUN)

                FRAME["LOG_SIZE"].append(float(line.split()[-2]))
                RUN += 1

    df = pd.DataFrame(FRAME)
    print(df.head())
    print(df.info())

    df.to_csv(f"{SAVE}/{args.implementation}.{datetime.datetime.now().isoformat(timespec='minutes').replace(':', '-')}.csv", index=False)


def add_args(parser: argparse.ArgumentParser):

    parser.add_argument(
        "-f",
        "--file",
        default="",
        type=str,
        help="File to parse.\n \n",
    )

    parser.add_argument(
        "-i",
        "--implementation",
        default="",
        type=str,
        help="Implementation.\n \n",
    )


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="parser.py",
        formatter_class=argparse.RawTextHelpFormatter,
        description="Parse results from an experiment file.",
        epilog="Created by Alejandro Ciuba, alc307@pitt.edu",
    )

    add_args(parser)
    args = parser.parse_args()

    main(args=args)
