from tikv_client import RawClient
import time

def main():
    # Time sleep
    time.sleep(30)

    # Connect to the TiKV cluster
    client = RawClient.connect(["pd1:2379","pd2:2379","pd3:2379"])

    # Writing data
    print("Putting data into TiKV")
    client.put(b"k1", b"Hello, TiKV!")
    client.put(b"k2", b"Hello, Python!")

    # Reading data
    print("Getting data from TiKV")
    value1 = client.get(b"k1")
    value2 = client.get(b"k2")
    print("k1:", value1)
    print("k2:", value2)

    # Scanning data
    print("Scanning data from k1 to k3")
    for key, value in client.scan(b"k1", end=b"k3"):
        print(f"{key}: {value}")

    # Close the client
    client.close()

if __name__ == "__main__":
    main()