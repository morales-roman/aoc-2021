arr = list(map(int,open('1.txt').read().splitlines()))

def first_part(arr):
    count = 0 
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            count+=1
    return count

def second_part(arr):
    sums=[]
    for i in range(len(arr)-2):
        sums.append(sum(arr[i:i+3]))
    return first_part(sums)


# print(len([x for x in output if x == "(increased)"]))

# print (first_part(arr))

print(second_part(arr))