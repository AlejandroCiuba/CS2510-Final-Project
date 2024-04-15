- Aync key-value access (`dict[key] = value`) does not guarantee up-to-date reads; use `dict.set`

- Suspicious of the `__raftlog` size https://github.com/bakwc/PySyncObj/blob/master/pysyncobj/journal.py#L42
