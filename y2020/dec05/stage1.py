from lib import *

def parse_boarding_pass(boarding_pass: str):
    row = boarding_pass[:7]
    row = row.replace("F", "0").replace("B", "1")
    row = int(row, 2)
    
    col = boarding_pass[7:]
    col = col.replace("L", "0").replace("R", "1")
    col = int(col, 2)
    
    return row, col

@timed
def stage(data: list[str]):
    # Year 2020 / Day 05 / Stage 1

    highest_seat_id = 0
    for boarding_pass in data:
        row, col = parse_boarding_pass(boarding_pass)
        seat_id = row * 8 + col
        print(f"{boarding_pass}: row {row}, col {col}, seat ID {seat_id}")
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id

    print(f"{GREEN_OK} Solution: {highest_seat_id}")
