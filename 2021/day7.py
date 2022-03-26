from pathlib import Path
import sys
from functools import cache

from numpy import result_type

cwd = Path.cwd()
input_path = cwd / "Inputs"


# with open(input_path / "sample7.txt", "r") as f:
with open(input_path / "day7.txt", "r") as f:
    crabs = [int(fish) for fish in f.read().split(",")]
    # print(crabs)
    # print(sum(crabs)/len(crabs))

@cache
def fuel_cost(x):
    return x*(x+1)//2

def efficient_position(crabs):
    min_x = min(crabs)
    max_x = max(crabs)
    least = sys.maxsize
    for x in range(min_x,max_x+1):
        value = sum([fuel_cost(abs(c-x)) for c in crabs])
        if value<least:
            least=value

    print(least)
    # print(result_map)
    # print(min(result_map,key=result_map.get))
    # print(sorted(result_map,key=result_map.get))

efficient_position(crabs)


