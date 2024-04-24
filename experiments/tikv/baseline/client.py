from tikv_client import RawClient
from timer import (Timer,
                   TimerVault)
from tqdm import tqdm
import threading
import argparse
import time
import requests

# Global variables, used for monitoring requests
collect_metrics = False;
prometheus_url = '' # TODO: get the ip of the Promethous container

# Make a request to Prometheus for any monitoring query
def fetch_prometheus_query(query):
    try:
        response = requests.get(f"{prometheus_url}/api/v1/query", params={'query': query})
        if response.status_code == 200:
            result = response.json()
            if result['status'] == 'success':
                return result['data']['result']['value'] # TODO: Make this get the singular value, check the JSON format
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch metrics: {str(e)}")
    return None

def main(args: argparse.Namespace):

    TEST = {f"{i:d}": f"{i:d}" for i in range(args.data)}
    TIMERVAULT = TimerVault("POST")
    metrics_dict = {'cpu': [], 'mem': []}

    # Connect to the TiKV cluster
    client = RawClient.connect(args.servers)

    for key in tqdm(TEST):
        # Timing from here not only because of server separation, but because connection is part of the library
        with Timer("put", TIMERVAULT):
            client.put(b"%s" % key.encode(), b"%s" % TEST[key].encode())
    
    # Specify parameters for utilization monitoring
    times = f'{1}m' # TODO: Replace this with a value corresponding to the length of time the send test ran for
    cpu_usage_query = f'avg_over_time(process_cpu_seconds_total[{times}])'
    memory_usage_query = f'avg_over_time(node_memory_MemTotal[{times}])'

    # Fetch CPU and memory metrics
    avg_cpu = fetch_prometheus_query(cpu_usage_query)
    ps_mem = fetch_prometheus_query(memory_usage_query)

    for key in tqdm(TEST):
        assert TEST[key] == f"{client.get(b'%s' % key.encode()).decode()}"
        print(f"{client.get(b'%s' % key.encode()).decode()}")

    times = TIMERVAULT.to_dict()['recordings']['total']

    print(f"RESULT | MESSAGES SENT/REQUESTED: {args.data}")
    print(f"RESULT | AVG COMMIT TIME: {sum(times) / len(times)}")
    print(f"RESULT | AVG CPU UTIL: {avg_cpu}%")
    print(f"RESULT | MAX MEM UTIL: {ps_mem / (2**10)} KiB")
    # print(f"RESULT | END LOG SIZE: {log_size} B")


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
