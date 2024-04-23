from tikv_client import RawClient
from tqdm import tqdm

import argparse
import time


def main(args: argparse.Namespace):

    TEST = {f"{i:d}": f"{i:d}" for i in range(args.data)}

    # Connect to the TiKV cluster
    client = RawClient.connect(["127.0.0.1:2379"])

    for key in tqdm(TEST):
        client.put(b"%s" % key.encode(), b"%s" % TEST[key].encode())

    for key in tqdm(TEST):
        assert TEST[key] == f"{client.get(b"%s" % key.encode()).decode()}"
        print(f"{client.get(b"%s" % key.encode()).decode()}")


def add_args(parser: argparse.ArgumentParser):

    parser.add_argument(
        "-d",
        "--data",
        default=1_000,
        type=int,
        help="Number of test values to generate.\n \n",
    )

    parser.add_argument(
        "-s",
        "--server",
        nargs="+",
        help="Server addresses with ports.\n \n",
    )

    parser.add_argument(
        "-k",
        "--skeleton",
        action="store_true",
        help="Add if it is a skeleton run. Spooky ooO!\n \n",
    )


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="client.py",
        formatter_class=argparse.RawTextHelpFormatter,
        description="Client class for the TiKV final project.",
        epilog="Created by Alejandro Ciuba, alc307@pitt.edu",
    )

    add_args(parser)
    args = parser.parse_args()

    main(args=args)
