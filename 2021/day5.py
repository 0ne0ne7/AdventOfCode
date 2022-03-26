from pathlib import Path
from functools import reduce
from pprint import pprint

cwd = Path.cwd()
input_path = cwd / "Inputs"


with open(input_path / "sample5.txt", "r") as f:
    lines = f.read().split('\n')
    lines = [[int(i.strip()) for i in line.replace('->',',').split(',')] for line in lines]
    # print(lines)

# for line in lines:


def plot(lines,part=1):
    max_coordinate = max([i for line in lines for i in line])+1
    # print(max_coordinate)
    coordinates = [[0]*max_coordinate for _ in range(max_coordinate)]
    for line in lines:
        x1=line[0]
        y1=line[2]
        x2=line[2]
        y2=line[3]
        slope = 'inf' if x1==x2 else (y2-y1)/(x2-x1)

        if (x1==x2) and (y1==y2):
            coordinates[x1][y1]+=1
        elif slope=='inf':
            x = x1
            min_y = min(y1,y2)
            max_y = max(y1,y2)
            for y in range(min_y,max_y+1):
                coordinates[y][x]+=1
        elif slope in (-1,0,1):
            min_x = min(x1,x2)
            max_x = max(x1,x2)
            for x in range(min_x,max_x+1):
                y = y1+slope*(x-x1)
                if y.is_integer():
                    coordinates[y][x]+=1
    pprint(coordinates)
    return sum([1 if p>1 else 0 for axis in coordinates for p in axis])

print(plot(lines))
print(plot(lines,part=2))