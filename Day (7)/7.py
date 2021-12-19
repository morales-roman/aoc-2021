from collections import defaultdict
from statistics import mean

# get input
data = defaultdict(int)
crabs = list(map(int, open("7.txt").read().split(",")))

def first_part(crabs):
    for i in range(len(crabs)):
        data[crabs[i]]+=1
    fuel_consumption = defaultdict(int)
    for i in range(len(crabs)):
        fuel = 0
        for crab, n_crabs in data.items():
            fuel += abs(crab - i) * n_crabs
            fuel_consumption[i] = fuel

    return min(fuel_consumption.values())

def part_two(crabs):
    mean_floor = int(mean(crabs))
    return sum(sum(range(abs(crab - mean_floor)+1)) for crab in crabs)

print(part_two(crabs))