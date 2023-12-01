from lib import *

def policy_matches(string):
    policy, password = string.split(": ")
    range_pw, key = policy.split(" ")
    left, right = range_pw.split("-")
    if len(password) < int(right) - 1:
        return False
    
    left_matches = password[int(left) - 1] == key
    right_matches = password[int(right) - 1] == key
    return left_matches ^ right_matches
    

@timed
def stage(data: list[str]):
    # Year 2020 / Day 02 / Stage 2
    matching_passwords = 0
    for line in data:
        if policy_matches(line):
            matching_passwords += 1

    print(f"{GREEN_OK} Solution: {matching_passwords}")
