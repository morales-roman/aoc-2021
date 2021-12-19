from itertools import permutations
def separate(arr):
    return [arr.split('|')[0], arr.split('|')[1]]

readings = list(map(separate, open("8.txt").read().splitlines()))

def part_one(readings):
    count = 0
    for reading in readings:
        numbers = reading[1].split()
        for number in numbers:
            if len(number) in (2,3,4,7):
                count+=1
    return count


with open("8.txt") as file:
    read_stream = file.read().strip().split("\n")

def part_two():
    answer = 0

    reading_numbers = {"acedgfb":8, "cdfbe":5, "gcdfa":2, "fbcad":3, "dab":7, "cefabd":9, "cdfgeb":6, "eafb":4, "cagedb":0, "ab":1}
    # sort each value in the dict
    reading_numbers = {"".join(sorted(key)):value for key,value in reading_numbers.items()}

    for line in read_stream:
        first_part,second_part = line.split(" | ")
        # first part
        first_part = first_part.split(" ")
        # second part
        second_part = second_part.split(" ")
        for perm in permutations("abcdefg"):
            permutation_map = {a:b for a,b in zip(perm,"abcdefg")}
            first_new = ["".join(permutation_map[c] for c in x) for x in first_part]
            second_new = ["".join(permutation_map[c] for c in x) for x in second_part]
            if all("".join(sorted(an)) in reading_numbers for an in first_new):
                second_new = ["".join(sorted(x)) for x in second_new]
                answer += int("".join(str(reading_numbers[x]) for x in second_new))
                break

    return answer

print(part_two())