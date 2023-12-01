from dataclasses import dataclass
from lib import *

def parse(data):
    passports = []
    passport = {}
    for line in data:
        if line == "":
            passports.append(passport)
            passport = {}
            continue
        for field in line.split(" "):
            key, value = field.split(":")
            passport[key] = value
    passports.append(passport)
    return passports

@timed
def stage(data: list[str]):
    # Year 2020 / Day 04 / Stage 1
    ok = 0
    for passport in parse(data):
        if len(passport) == 8 or (len(passport) == 7 and "cid" not in passport):
            ok += 1
    print(f"{GREEN_OK} Solution: {ok}")
