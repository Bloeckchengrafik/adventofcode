from lib import *

def policy_matches(string):
    policy, password = string.split(": ")
    range_pw, key = policy.split(" ")
    min_pw, max_pw = range_pw.split("-")
    count = 0
    for letter in password:
        if letter == key:
            count += 1
    return int(min_pw) <= count <= int(max_pw)

@timed
def stage(data: list[str]):
    # Year 2020 / Day 02 / Stage 1
    matching_passwords = 0
    for line in data:
        if policy_matches(line):
            matching_passwords += 1

    print(f"{GREEN_OK} Solution: {matching_passwords}")
