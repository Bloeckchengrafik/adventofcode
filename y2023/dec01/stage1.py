from lib import *

@timed
def stage(data: list[str]):
    s = 0
    for i in data:
        digits = [x for x in i if x in "0123456789"]
        s += int(digits[0] + digits[-1])

    print(f"{GREEN_OK} SUM={s}")
