# Client for the server
from tqdm import tqdm

import argparse
import requests


def http(url):
    return f"http://{url}"


def main(args: argparse.Namespace):

    TEST = {f"TESTKEY{i:d}": f"TESTVALUE{i:d}" for i in range(args.data)}
    SERVERS = args.servers

    # Get and connect directly to the leader
    response = requests.get(f"{SERVERS[0]}/node/status")
    metadata = response.json()
    LEADER = f"http://{metadata['leader'].split(':')[0]}:5000"

    for key in tqdm(TEST):

        response = requests.post(f"{LEADER}/user/{key}/{TEST[key]}")
        value = response.json()

        try:
            assert TEST[key] == value[key]
        except AssertionError:
            print(f"{key}: {TEST[key]} | {value}")

    for node in SERVERS:
        print(requests.get(f"{node}/node/status").json())
    
    for key in tqdm(TEST):

        response = requests.get(f"{LEADER}/user/{key}")
        value = response.json()

        try:
            assert TEST[key] == value[key]
        except AssertionError:
            print(f"{key}: {TEST[key]} | {value}")

    for node in SERVERS:
        print(requests.get(f"{node}/node/status").json())

    timer_info = requests.get(f"{LEADER}/node/metadata").json()
    print(timer_info)
    times = timer_info["recordings"]["total"]

    print(f"RESULT | AVG COMMIT TIME: {sum(times) / len(times)}")


def add_args(parser: argparse.ArgumentParser):

    parser.add_argument(
        "-d",
        "--data",
        default=100,
        type=int,
        help="Number of test values to generate.\n \n",
    )

    parser.add_argument(
        "-s",
        "--servers",
        nargs="+",
        type=http,
        help="Server addresses with ports.\n \n",
    )


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="client.py",
        formatter_class=argparse.RawTextHelpFormatter,
        description="Client class for the PySyncObj final project.",
        epilog="Created by Alejandro Ciuba, alc307@pitt.edu",
    )

    add_args(parser)
    args = parser.parse_args()

    main(args=args)

