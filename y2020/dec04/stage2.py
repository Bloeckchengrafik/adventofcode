from lib import *
from y2020.dec04.stage1 import parse

def validate(passport):
    byr = int(passport["byr"])
    if byr < 1920 or byr > 2002:
        print(f"{RED_ERR} byr: {byr}")
        return False
    
    iyr = int(passport["iyr"])
    if iyr < 2010 or iyr > 2020:
        print(f"{RED_ERR} iyr: {iyr}")
        return False
    
    eyr = int(passport["eyr"])
    if eyr < 2020 or eyr > 2030:
        print(f"{RED_ERR} eyr: {eyr}")
        return False
    
    hgt = passport["hgt"]
    if hgt.endswith("cm"):
        hgt = int(hgt[:-2])
        if hgt < 150 or hgt > 193:
            print(f"{RED_ERR} hgt: {hgt}")
            return False
    elif hgt.endswith("in"):
        hgt = int(hgt[:-2])
        if hgt < 59 or hgt > 76:
            print(f"{RED_ERR} hgt: {hgt}")
            return False
    else:
        print(f"{RED_ERR} hgt: {hgt}")
        return False
    
    hcl = passport["hcl"]
    if not hcl.startswith("#"):
        print(f"{RED_ERR} hcl: {hcl}")
        return False
    if len(hcl) != 7:
        print(f"{RED_ERR} hcl: {hcl}")
        return False
    
    ecl = passport["ecl"]
    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        print(f"{RED_ERR} ecl: {ecl}")
        return False
    
    pid = passport["pid"]
    if len(pid) != 9:
        print(f"{RED_ERR} pid: {pid}")
        return False
    
    print(f"{GREEN_OK} Passport {passport}")
    return True

@timed
def stage(data: list[str]):
    # Year 2020 / Day 04 / Stage 2
    passports = [x for x in parse(data) if len(x) == 8 or (len(x) == 7 and "cid" not in x)]
    passports = [x for x in passports if validate(x)]
    print(f"{GREEN_OK} Solution: {len(passports)}")
