import time
from rich import print
from dataclasses import dataclass
import re
from rich.progress import track as progress
from rich.progress import track
from math import *

GREEN_OK = "[[bold green]OK[/bold green]]"
RED_ERR = "[[bold red]ERR[/bold red]]"
YELLOW_INFO = "[[bold yellow]INFO[/bold yellow]]"

def timed(fn):
    def _wr(*args):
        nanos = time.perf_counter_ns()
        fn(*args)
        end = time.perf_counter_ns()
        print(f"[[bold yellow]TIME[/bold yellow]] Time: {end - nanos} ns ({(end - nanos) / 1000000} ms)")

    return _wr
    

def lmap(func, *iterables):
    return list(map(func, *iterables))

def ints(s: str) -> list[int]:
    assert isinstance(s, str), f"you passed in a {type(s)}!!!"
    return lmap(int, re.findall(r"(?:(?<!\d)-)?\d+", s))