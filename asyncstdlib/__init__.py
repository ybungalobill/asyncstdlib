"""The missing ``async`` toolbox"""
from .builtins import (
    anext,
    zip,
    map,
    filter,
    enumerate,
    iter,
    all,
    any,
    max,
    min,
    sum,
    list,
    dict,
    set,
    tuple,
)
from .functools import reduce, lru_cache, cached_property
from .contextlib import closing, contextmanager, nullcontext, ExitStack
from .itertools import (
    accumulate,
    cycle,
    chain,
    compress,
    dropwhile,
    islice,
    takewhile,
    starmap,
    tee,
    zip_longest,
    groupby,
)

__version__ = "1.0.0"

__all__ = [
    "anext",
    "zip",
    "map",
    "filter",
    "enumerate",
    "iter",
    "all",
    "any",
    "max",
    "min",
    "sum",
    "list",
    "dict",
    "set",
    "tuple",
    # functools
    "reduce",
    "lru_cache",
    "cached_property",
    # contextlib
    "closing",
    "contextmanager",
    "nullcontext",
    "ExitStack",
    # itertools
    "accumulate",
    "cycle",
    "chain",
    "compress",
    "dropwhile",
    "takewhile",
    "islice",
    "starmap",
    "tee",
    "zip_longest",
    "groupby",
]
