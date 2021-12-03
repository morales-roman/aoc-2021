arr = list(map(str, open("3.txt").read().splitlines())) 

def count_freq(numbers, index):
    frequencies = {"0": 0, "1": 0}
    for num in numbers:
        frequencies[num[index]] += 1
    return frequencies

def common_bit(numbers, index, common_value:bool):
    # common_value True is for most common
    # common_value False is for least common
    freqs = count_freq(numbers, index)
    print(freqs)
    if common_value:
        return "1" if freqs["1"] >= freqs["0"] else "0"
    else:
        return "0" if freqs["1"] >= freqs["0"] else "1"

def extract_from_array(numbers, index, bit):
    return [number for number in numbers if number[index] == bit]


def extract_until_one_remains(numbers, common_boolean):
    index = 0
    while len(numbers) > 1:
        bit_value = common_bit(numbers, index, common_boolean) if common_boolean else common_bit(numbers, index, common_boolean)
        numbers = extract_from_array(numbers, index, bit_value)
        index += 1
    return numbers[0]



oxygen_generator_rating = extract_until_one_remains(arr, True)

co2_scrubber_rating = extract_until_one_remains(arr, False)

print(int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2))