# Client for the server
import json
import requests


TEST = {f"TESTKEY{i:d}": f"TESTVALUE{i:d}" for i in range(10)}
SERVER = "http://localhost:6000"
OTHERS = ["http://localhost:6001", 
          "http://localhost:6002", ]
ALL = [*OTHERS, SERVER]

def main():

    for node in ALL:
        print(requests.get(f"{node}/node/status").json())

    for key in TEST:
        response = requests.post(f"{SERVER}/user/{key}/{TEST[key]}")
        print(f"POSTED {key}-{TEST[key]} | {response.json()}")

    for node in ALL:
        print(requests.get(f"{node}/node/status").json())
    
    for key in TEST:
        response = requests.get(f"{SERVER}/user/{key}")
        value = response.json()
        print(f"{key}: {TEST[key]} | {value}")

    for node in ALL:
        print(requests.get(f"{node}/node/status").json())

    print(requests.get(f"{SERVER}/node/metadata").json())


if __name__ == "__main__":
    main()
