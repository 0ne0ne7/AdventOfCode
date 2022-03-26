from pathlib import Path

cwd = Path.cwd()
input_path = cwd / 'Inputs'

with open(input_path/'day2.txt','r') as f:
    input_list = f.read().strip().split("\n")
    input_list = [cmd.split(" ") for cmd in input_list]
    # input_list = [(i,int(j)) for cmd in input_list for i,j in cmd]
    # print(input_list)
    # input_list = [int(i) for i in input_list]

def part1(input):
    horizontal, depth, aim = 0,0,0
    for cmd in input:
        # print(cmd)
        # print(cmd[0])
        if cmd[0]=='forward':
            horizontal+=int(cmd[1])
            # depth+=aim*int(cmd[1])
        if cmd[0]=='up':
            depth-=int(cmd[1])
            # aim-=int(cmd[1])
        if cmd[0]=='down':
            depth+=int(cmd[1])
            # aim+=int(cmd[1])
    print(horizontal*depth)

def part2(input):
    horizontal, depth, aim = 0,0,0
    for cmd in input:
        # print(cmd)
        # print(cmd[0])
        if cmd[0]=='forward':
            horizontal+=int(cmd[1])
            depth+=aim*int(cmd[1])
        if cmd[0]=='up':
            # depth-=int(cmd[1])
            aim-=int(cmd[1])
        if cmd[0]=='down':
            # depth+=int(cmd[1])
            aim+=int(cmd[1])
    print(horizontal*depth)

part1(input_list)
part2(input_list)