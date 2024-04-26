# CS2510-Final-Project
---
[Alejandro Ciuba](https://alejandrociuba.github.io), Winston Osei-Bonsu
---
## Summary

![Outline of our project's experiment pipeline](cs2510-final.png "Experiment Pipeline")

This is the repository containing the code for their Spring 2024 CS2510 Final Project by Alejandro Ciuba and Winston Osei-Bonsu. Each implementation has its own folder for all server components (bash script, Dockerfile etc.) in `implementations/`. All implementations also have their own simulation and Docker-Compose set-up under their `<name>/baseline/` folder in `experiments/`. Lastly, please make sure you are online as we pull from [this repository](https://github.com/AlejandroCiuba/hraftd) when running HashiCorp's implementation inside the server's Dockerfile.

### Repository Structure:
- `.CS2510_Project_Proposal.pdf`: Original Project Proposal
- `notes.md`: Most subdirectories will have this too; any notes we track.
- `README.md`: This...
- `experiments/`: Results from experiments.
- `implementations/`: Raft implementations.
- `other/`: Other functions/packages/whatever.
- `raftdata/`: Implementation data gotten from the table at the [official Raft website](https://raft.github.io).
---
## Run Experiments
### Full Implementations

To run any given raft implementation experiments:

1. Navigate to the `experiments/` folder
```bash
cd experiments
```

2. Run the following command to start a single run of the simulation for the API:
```bash
sudo bash run.sh baseline <pysyncobj | hashicorp>
```
**NOTE:** To run TiKV, you **must pass in your IP address**. On Linux, you can run `ifconfig -a` and find your IP. Then run:
```bash
sudo bash run.sh baseline tikv <ip>
```

3. Check the results for that run in the `results/` folder

### Skeleton Implementations

To run the skeleton version of a server:
```bash
sudo bash run.sh baseline <pysyncobj | hashicorp> skeleton
```
**NOTE:** TiKV does not have a skeleton implementation. It actually utilizes the skeleton environment variable to give the Docker Compose the IP address.

### Batch Simulations

You can run multiple simulations for a given implementation back-to-back by running:
```bash
sudo bash batch_run.sh baseline <implementation> <number of runs> <skeleton | ip>
```
This will put the runs in the `results/` folder and also (for HashiCorp and PySyncObj) make a CSV file in `results_csv/`. It will return an error at this point for TiKV, but this is because the `parser.py` script is for the other two. It will still make a results text file in `results/`

### Obtain Packet Information

If you wish to get packet information either during a single run or during a batch of runs:

1. Download and set-up [WireShark](https://www.wireshark.org).

2. Download the [EdgeShark Plugin](https://github.com/siemens/edgeshark).

3. Run their Docker Compose file as described in their README.md; make sure you also launch the localhost website.

4. Start the run or batch of runs as described in either [Full Implementations](#full-implementations), [Skeleton Implementations](#skeleton-implementations), or [Batch Simulations](#batch-simulations).

5. Refresh the EdgeShark webpage until `baseline-defaults` becomes green. This means it is up and being tracked by EdgeShark.

6. Click the sharkfin to the right of `baseline-defaults`, this should launch WireShark and begin the packet-sniffing process.

7. Once all packets have been sniffed, save it and filter by `servera` ports to see the total number of packets. Divide this number by ten.
    **NOTE:** For TiKV, you must filter by all server ports via `tcp.port in {20160..20168}` in WireShark's filter.

**IF YOU CANNOT GET THIS PART TO WORK, EMAIL alejandrociuba@pitt.edu AND HE CAN SEND THE `.pcapng` INFORMATION!!!**
