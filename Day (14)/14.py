from collections import defaultdict, Counter


# read file
with open("14.txt") as file:
    polymer = next(file).strip()
    equivalents = file.read().splitlines()
    rules = defaultdict(str)
    for i in equivalents:
        if len(i)!=0:
            rules[i.split(' -> ')[0]] = i.split(' -> ')[1]

def part_one(values_rules:set, polymer:list, polymer_range:int):
    letter_count = defaultdict(int)
    for i in polymer:
        letter_count[i]+=1
    
    
    for _ in range(polymer_range):
        new_polymer = ""
        for index in range(1,len(polymer)):
            pair = polymer[index-1] +''+polymer[index]
            letter = values_rules[pair]
            new_polymer += pair[0] + letter
            letter_count[letter]+=1
        polymer = new_polymer + polymer[-1]
    
    return max(letter_count.values())-min(letter_count.values())

def part_two(values_rules:set, polymer:list, polymer_range:int):
    letter_count = Counter(polymer[i:i + 2] for i in range(len(polymer) - 1))
    
    for _ in range(polymer_range):
        counter_update = Counter()
        for pair, count in letter_count.items():
            inserting = values_rules[pair]
            counter_update[pair[0] + inserting] += count
            counter_update[inserting + pair[1]] += count
        letter_count = counter_update
    
    counts = Counter()
    for (_,right_part), count in letter_count.items():
        counts[right_part] += count
    
    # Add missing character from the slicing
    counts[polymer[0]] += 1

    return max(counts.values()) - min(counts.values())


print(part_two(rules,polymer, 40))