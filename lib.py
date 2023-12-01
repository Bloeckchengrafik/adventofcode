import time
from rich import print

GREEN_OK = "[[bold green]OK[/bold green]]"
RED_ERR = "[[bold red]ERR[/bold red]]"

def timed(fn):
    def _wr(*args):
        nanos = time.time_ns()
        fn(*args)
        end = time.time_ns()
        print(f"[[bold yellow]TIME[/bold yellow]] Time: {end - nanos} ns ({(end - nanos) / 1000000} ms)")

    return _wr
    