from lib import *

number_names = [
    ("one", "one1one"),
    ("two", "two2two"),
    ("three", "three3three"),
    ("four", "four4four"),
    ("five", "five5five"),
    ("six", "six6six"),
    ("seven", "seven7seven"),
    ("eight", "eight8eight"),
    ("nine", "nine9nine"),
]
@timed
def stage(data: list[str]):
    s = 0
    for i in data:
        for a, b in number_names:
            i = i.replace(a, b)

        digits = [x for x in i if x in "0123456789"]
        s += int(digits[0] + digits[-1])

    print(f"{GREEN_OK} SUM={s}")
