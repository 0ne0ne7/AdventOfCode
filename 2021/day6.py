from pathlib import Path

cwd = Path.cwd()
input_path = cwd / "Inputs"


with open(input_path / "day6.txt", "r") as f:
    fish = [int(fish) for fish in f.read().split(",")]
    # print(fish)

def part1(fish,days):
    current_fish = fish.copy()
    for day in range(days):
        # print(current_fish)
        # print(f'The day is {day}')
        babies = [9]*sum([1 if timer==0 else 0 for timer in current_fish])
        # print(f'babies are {len(babies)}')
        current_fish = current_fish+babies
        current_fish = [(timer-1)%7 if timer<1 else timer-1 for timer in current_fish]

    # print(current_fish)
    # print(len(current_fish))
    return len(current_fish)


# print(part1(fish,80))
# par1 is memory intensive
def growth(fish,days):
    current_fish = fish.copy()
    status = [fish.count(k) for k in range(9)]
    # print(status)
    while days:
        babies = status[0]
        for idx in range(8):
            status[idx]=status[idx+1]
        status[6]+=babies
        status[8]=babies
        days=days-1

    # print(status)
    print(sum(status))


growth(fish,18)
growth(fish,80)
growth(fish,256)

