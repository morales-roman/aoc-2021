def do_list(itrr: str):
    return [itrr.split()[0],int(itrr.split()[1])]

arr = list(map(do_list,open('second.txt').read().splitlines()))

def first(arr):
    x,depth = 0,0

    for item in arr:
        if item[0]=="forward":
            x+=item[1]
        elif item[0] == "down":
            depth+=item[1]
        elif item[0] == "up":
            depth-=item[1]

    return x * depth

def second(arr):
    x,aim,depth = 0,0,0

    for item in arr:
        if item[0]=="forward":
            x+=item[1]
            depth+=item[1]*aim
        elif item[0] == "down":
            aim+=item[1]
        elif item[0] == "up":
            aim-=item[1]
            
    return x * depth

print(second(arr))