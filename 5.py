from collections import defaultdict

def do_list(itrr: str):
    return [int(x) for x in itrr.split(" -> ")[0].split(',')], [int(x) for x in itrr.split(" -> ")[1].split(',')]

arr = list(map(do_list,open('5.txt').read().splitlines()))

def build_terrain(arr, terrain) -> set:
    for line in arr:
        first_x,first_y,second_x,second_y = line[0][0], line[0][1], line[1][0], line[1][1]
        # check if values are in a straight line
        if first_x == second_x or first_y == second_y:
            # check if value on x or y are going up or down and calculate range from there
            x_range = list(range(first_x, second_x-1, -1)) if first_x > second_x else list(range(first_x, second_x+1))
            y_range = list(range(first_y, second_y-1, -1)) if first_y > second_y else list(range(first_y, second_y+1))
            
            # populate all possible coordinates between points
            if len(x_range) > len(y_range):
                ranges = ["%s, %s" % (x_, y_range[0]) for x_ in x_range]
            else:
                ranges = ["%s, %s" % (x_range[0], y_) for y_ in y_range]
        
            for range_ in ranges:
                terrain[range_]+=1

    return terrain

def terrain_covered(covered_terrain:set) -> int:
    overlaps = 0
    for coordinate, ocurr in covered_terrain.items():
        if ocurr > 1:
            overlaps+=1
    return overlaps

terrain = defaultdict(int)

terrain = build_terrain(arr , terrain)
print(terrain_covered(terrain))