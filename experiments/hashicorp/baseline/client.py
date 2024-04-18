# Client for the server
from tqdm import tqdm

import argparse
import json
import requests


def http(url):
    return f"http://{url}"


def main(args: argparse.Namespace):

    TEST = {f"{i:d}": f"{i:d}" for i in range(args.data)}
    LEADER = args.server

    for key in tqdm(TEST):
        requests.post(f"{LEADER}/key", data=json.dumps({key: TEST[key]}))

    for key in tqdm(TEST):
        requests.get(f"{LEADER}/key/{key}")

    results = requests.get(f"{LEADER}/stats")
    print(results.json())

    time = results['avg']
    avg_cpu = results['cpu']
    ps_mem = results['rss']
    log_size = results['log']

    # if "test" in metadata.keys():
    #     print("RESULTS ARE FROM A SKELETON")

    print(f"RESULT | MESSAGES SENT/REQUESTED: {args.data}")
    print(f"RESULT | AVG COMMIT TIME: {time}")
    print(f"RESULT | AVG CPU UTIL: {avg_cpu}%")
    print(f"RESULT | MAX MEM UTIL: {ps_mem / (2**20)} MiB")
    print(f"RESULT | END LOG SIZE: {log_size} B")


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
        type=http,
        help="Server addresses with ports.\n \n",
    )


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="client.py",
        formatter_class=argparse.RawTextHelpFormatter,
        description="Client class for the Hashicorp final project.",
        epilog="Created by Alejandro Ciuba, alc307@pitt.edu",
    )

    add_args(parser)
    args = parser.parse_args()

    main(args=args)

