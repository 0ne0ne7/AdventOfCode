from pathlib import Path

cwd = Path.cwd()
input_path = cwd / "Inputs"

sample = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010"
]
with open(input_path / "day3.txt", "r") as f:
    input_list = f.read().strip().split("\n")
    # print(input_list)

def part1(input):
    gamma = list(input[0])
    epslion = list(input[0])
    # print(len(result))
    for i in range(len(gamma)):
        bits = [int(cmd[i]) for cmd in input]
        # print(bits)
        max_bit = max(set(bits), key=bits.count)
        gamma[i] = str(max_bit)
        epslion[i] = str(1-max_bit)
    print(int(("".join(gamma)),2)*int(("".join(epslion)),2))

def part2(input):
    o2_list = input
    co2_list = input
    for i in range(len(input[0])):
        if len(o2_list)>1:
            bits = [int(cmd[i]) for cmd in o2_list]
            max_bit = 1 if sum(bits)*2-len(o2_list)>=0 else 0
            o2_list = [cmd for cmd in o2_list if int(cmd[i])==max_bit]
        else:
            break
    for i in range(len(input[0])):
        if len(co2_list)>1:
            bits = [int(cmd[i]) for cmd in co2_list]
            min_bit = 0 if sum(bits)*2-len(co2_list)>=0 else 1
            co2_list = [cmd for cmd in co2_list if int(cmd[i])==min_bit]
        else:
            break

    print(int(o2_list[0],2)*int(co2_list[0],2))

# part1(sample)
# part1(input_list)
part2(sample)
part2(input_list)