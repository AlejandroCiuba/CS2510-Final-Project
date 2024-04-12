# A universal 
from __future__ import annotations
from collections import defaultdict
from contextlib import contextmanager

import time


class Timer:
    """
    Timer to measure the process time spent on given calls for any Python code.
    """

    name: str
    vault: TimerVault
    auto_add: bool  # Automatically add itself upon running `__exit()__`

    total: float
    start: float
    stop: float

    def __init__(self, name: str, vault: TimerVault, auto_add: bool = True):
        """
        Parameters
        ---

        `name`: `str`
            Name of the function group

        `vault`: `TimerVault`
            `TimerVault` instance to hook this up to

        `auto_add`: `bool`
            Automatically add itself to its `TimerVault` upon `__exit()__`; default `True`
        """

        self.name = name
        self.vault = vault
        self.auto_add = auto_add

    def __enter__(self):

        self.start = time.process_time()
        return self
    
    def __exit__(self, type, value, traceback):
        
        self.stop = time.process_time()
        self.total = self.stop - self.start

        if self.auto_add:
            self.vault.add(self)

    def to_dict(self):
        """
        Returns
        ---

        `dict[name: str, list[total: float, start: float, stop: float]]`
        """
        return {self.name: [self.total, self.start, self.stop]}


class TimerVault:
    """
    Store multiple times for different function calls.
    Useful if you want to dump time results at the end.
    """

    times: dict
    timers: list[Timer]
    _vault_name: str
    _call_id: int

    def __init__(self, vault_name: str):
        """
        Parameters
        ---

        `vault_name`: `str`
            Name to identifiy this vault
        """

        self._vault_name = vault_name
        self.timers = []
        self.times = defaultdict(list)
        self._call_id = 0

    def add(self, timer: Timer):
        """
        Add a specific `Timer` to this vault's database.

        Parameters
        ---

        `timer`: `Timer`
            The instance whose data will be added
        """

        self.timers.append(timer)

        d = timer.to_dict()
        for k in d:

            self.times["timer"].append(k)
            self.times["total"].append(d[k][0])
            self.times["start"].append(d[k][1])
            self.times["stop"].append(d[k][2])
            self.times["call"].append(self._call_id)

            self._call_id += 1

    def to_dict(self):
        """
        Returns
        ---

        A dictionary containing the metadata for the vault and its stored timer values.
        """
        return {"vault": self._vault_name,
                "recordings": dict(self.times)}


@contextmanager
def measure():

    start = time.process_time()  # Should I use perf_counter?

    try:
        yield
    finally:
        print(time.process_time() - start)


if __name__ == "__main__":

    # Create a TimerVault to store times
    tv = TimerVault("Functions to time")

    # Timers measure specific groups of function calls
    with Timer("Function Group 1", tv):
        print("Hello, World")

    # Different group = different calls
    with Timer("Function Group 2", tv):
        print("Yo")
        print("You can measure groups of functions too")

    # Same as the first group in essence
    with Timer("Function Group 1", tv):
        print("Hello, World")

    print(tv.to_dict())
