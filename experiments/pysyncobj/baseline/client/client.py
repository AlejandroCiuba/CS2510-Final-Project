# Client for the server
import argparse
import requests


def http(url):
    return f"http://{url}"


def main(args: argparse.Namespace):

    TEST = {f"TESTKEY{i:d}": f"TESTVALUE{i:d}" for i in range(10)}
    SERVERS = args.servers

    for node in SERVERS:
        print(requests.get(f"{node}/node/status").json())

    for key in TEST:
        response = requests.post(f"{SERVERS[0]}/user/{key}/{TEST[key]}")
        print(f"POSTED {key}-{TEST[key]} | {response.json()}")

    for node in SERVERS:
        print(requests.get(f"{node}/node/status").json())
    
    for key in TEST:
        response = requests.get(f"{SERVERS[0]}/user/{key}")
        value = response.json()
        print(f"{key}: {TEST[key]} | {value}")

    for node in SERVERS:
        print(requests.get(f"{node}/node/status").json())

    print(requests.get(f"{SERVERS[0]}/node/metadata").json())


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

