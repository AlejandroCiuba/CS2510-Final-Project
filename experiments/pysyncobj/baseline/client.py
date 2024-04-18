# Client for the server
from tqdm import tqdm

import argparse
import requests


def http(url):
    return f"http://{url}"


def main(args: argparse.Namespace):

    TEST = {f"{i:d}": f"{i:d}" for i in range(args.data)}
    SERVERS = args.servers

    # Get and connect directly to the leader
    response = requests.get(f"{SERVERS[0]}/node/status")
    metadata = response.json()
    LEADER = f"http://{metadata['leader'].split(':')[0]}:5000"

    for key in tqdm(TEST):

        response = requests.post(f"{LEADER}/user/{key}/{TEST[key]}")
        value = response.json()
        assert TEST[key] == value[key], f"{key}: {TEST[key]} | {value}"

    for node in SERVERS:
        print(requests.get(f"{node}/node/status").json())
    
    for key in tqdm(TEST):

        response = requests.get(f"{LEADER}/user/{key}")
        value = response.json()
        assert TEST[key] == value[key], f"{key}: {TEST[key]} | {value}"

    for node in SERVERS:
        print(requests.get(f"{node}/node/status").json())

    results = requests.get(f"{LEADER}/node/metadata").json()

    print(results)

    times = results["vault"]["recordings"]["total"]
    avg_cpu = results["avg_cpu"]
    ps_mem = results["ps_mem"]
    log_size = results["log_size"]

    if "test" in metadata.keys():
        print("RESULTS ARE FROM A SKELETON")

    print(f"RESULT | MESSAGES SENT/REQUESTED: {args.data}")
    print(f"RESULT | AVG COMMIT TIME: {sum(times) / len(times)}")
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

