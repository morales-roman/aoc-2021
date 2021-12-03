arr = list(map(str, open("3.txt").read().splitlines()))

def count_freq(arr):
    num_length = len(arr[0])
    frequencies = [{"0": 0, "1": 0} for x in range(num_length)]
    
    for num in arr:
        for i,digit in enumerate(num):
            frequencies[i][digit] += 1
    
    return frequencies

def most_common(freq):
    most_common_arr = []
    for i in range(len((freq))):
        most_common_arr.append([key for key, value in freq[i].items() if value == max(freq[i]["0"],freq[i]["1"])][0])
    return "".join(most_common_arr)

def epsilon(most_common):
    return "".join(['1' if letter == '0' else '0' for letter in most_common ])




most_common_num = most_common(count_freq(arr))
epsilon_num = epsilon(most_common_num)

# first answer
print (int(most_common_num,2)*int(epsilon_num,2))

