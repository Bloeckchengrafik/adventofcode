import os.path
import typer
import sys

app = typer.Typer()


@app.command()
def run(year: int, day: int, stage: int, file: str = typer.Option(..., "--file", "-f", help="Input file")):
    if not os.path.exists(file):
        typer.echo(typer.style(f"File {file} does not exist", fg=typer.colors.WHITE, bg=typer.colors.RED))
        raise typer.Exit(1)

    with open(file) as f:
        data = f.readlines()

    data = [line.replace("\n", "").replace("\r", "") for line in data]

    # load and exec
    day = str(day)
    if len(day) < 2:
        day = "0" + day

    filename = "y"+str(year)+"/dec"+str(day)+"/stage"+str(stage)+".py"
    with open(filename, "r") as f:
        content = f.read()
    with open("tmp.py", "w") as f:
        f.write(content)

    from tmp import stage
    stage(data)

    os.remove("tmp.py")

    
@app.command()
def gen_day(year: int, day: int):
    # Make sure there is a year directory
    if not os.path.exists("y"+str(year)):
        os.makedirs(str(year))

    day = str(day)
    if len(day) < 2:
        day = "0" + day

    folder = "y"+str(year)+"/dec"+day
    if not os.path.exists(folder):
        os.makedirs(folder)

    filecontent = f"""from lib import *

@timed
def stage(data: list[str]):
    # Year {year} / Day {day} / Stage <S>
    pass
"""
    
    with open(f"{folder}/stage1.py", "w") as f:
        f.write(filecontent.replace("<S>", "1"))

    
    with open(f"{folder}/stage2.py", "w") as f:
        f.write(filecontent.replace("<S>", "2"))
    
        

if __name__ == "__main__":
    app()