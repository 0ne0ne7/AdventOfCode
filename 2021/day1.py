from pathlib import Path

cwd = Path.cwd()
input_path = cwd / 'Inputs'

with open(input_path/'day1.txt','r') as f:
    data = f.read()
    input_list = data.split("\n")
    input_list = [int(i) for i in input_list]

# print(input_list)
# print(input_list[-1])
sample = [199,200,208,210,200,207,240,269,260,263]


def part1(input):
    result = [first<second for first, second in zip(input,input[1:])]
    print(sum(result))

def part2(input):
    result = [first+second+third for first, second, third in zip(input,input[1:],input[2:])]
    return part1(result)


part1(input_list)
part2(input_list)
part1(sample)
part2(sample)
