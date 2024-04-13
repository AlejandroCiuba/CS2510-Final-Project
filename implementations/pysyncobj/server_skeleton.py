# To account for our implementation overhead 
from flask import Flask
# from pysyncobj import SyncObj
# from pysyncobj.batteries import ReplDict
from timer import (Timer,
                   TimerVault, )

import argparse
import json
import os
import psutil

app: Flask = Flask(__name__)


# Metrics information
TIMERVAULT: TimerVault = TimerVault("PySyncObj")
PROC: psutil.Process = psutil.Process(os.getpid())

# DB: ReplDict = ReplDict()
# SYNCOBJ: SyncObj


@app.get("/user/<key>")
def user_get(key: str):
    return json.dumps({key: key}), 201


@app.post("/user/<key>/<value>")
def user_post(key: str, value: str):

    with Timer("add", TIMERVAULT):
        assert key == key

    return json.dumps({key: value}), 201


@app.get("/node/status")
def node_status():

    # status = SYNCOBJ.getStatus()
    # safe_status = {k: str(status[k]) for k in status}
    return json.dumps({"leader": "serverA:6000",
                       "test": "skeleton"}), 201


@app.get("/node/ready")
def node_ready():
    return json.dumps({"ready": "lol"}), 201


@app.get("/node/metadata")
def node_metadata():

    metadata = {"vault": TIMERVAULT.to_dict(),
                "avg_cpu": PROC.cpu_percent(),
                "ps_mem": PROC.memory_info().rss / (2**20),  # MB
                "log_size": 0}

    return json.dumps(metadata), 201


def main(args: argparse.Namespace):

    node = f"{args.ip}:{args.port}"

    # global SYNCOBJ
    # SYNCOBJ = SyncObj(node, args.nodes, consumers=[DB])

    # print(SYNCOBJ.isReady())
    app.run(host=args.ip, port=args.service_port)


def add_args(parser: argparse.ArgumentParser):

    parser.add_argument(
        "-i",
        "--ip",
        type=str,
        default="localhost",
        help="Server IP address.\n \n",
    )

    parser.add_argument(
        "-p",
        "--port",
        type=str,
        default=5000,
        help="Server connection port for nodes.\n \n",
    )

    parser.add_argument(
        "-s",
        "--service_port",
        type=str,
        default=50051,
        help="Server connection port for clients.\n \n",
    )

    parser.add_argument(
        "-n",
        "--nodes",
        nargs="+",
        type=str,
        help="Other nodes' addresses with ports.\n \n",
    )

    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="Other nodes' addresses with ports.\n \n",
    )


if __name__ == "__main__":

    PROC.cpu_percent()

    parser = argparse.ArgumentParser(
        prog="server.py",
        formatter_class=argparse.RawTextHelpFormatter,
        description="Server for PySyncObj",
        epilog="Created by Alejandro Ciuba, alc307@pitt.edu",
    )

    add_args(parser)
    args = parser.parse_args()

    main(args=args)
