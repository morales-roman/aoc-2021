def part_one():
    tank = list(map(int, open("6.txt").read().split(",")))
    # naive solution since it goes exponential: O(n!)
    for i in range(80):
        for i in range(len(tank)):
            if tank[i] == 0:
                tank[i] = 6
                tank.append(8)
            else:
                tank[i]-=1
    
    return len(tank)

def part_two():
    # optimal approach, it basically classify each fish into tanks of their upcoming newborn release: O(n)
    # range is not inclusive and we need the maximum days of a lanternfish newborn which is 8
    tank = {x:0 for x in range(9)}
    with open("6.txt") as file:
        for line in file:
            for fsh in map(int, line.split(",")):
                tank[fsh] += 1

    for i in range(256):
        zero_day_qty = tank[0]
        # move upper values to lower levels
        for j in range(0, 8):
            tank[j] = tank[j+1]
        tank[8] = zero_day_qty
        tank[6] += zero_day_qty

    return sum(tank.values())



print(part_one())

# print(part_two())