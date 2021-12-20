from collections import defaultdict, deque

input_brackets = list(open("10.txt").read().splitlines())
pairs = {'(':')','[':']','{':'}','<':'>'}
closings = {v for k,v in pairs.items()}
syntax_error_scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
autocomplete_scores = {')': 1, ']': 2, '}': 3, '>': 4}

def part_one(input_b:list, pairs:set, scores:set)-> int:
    stack = deque()
    score = 0
    for inp in input_b:
        for ch in inp:
            if ch in pairs:
                stack.appendleft(pairs[ch])
            elif ch != stack.popleft():
                score += scores[ch]
                break
    return score

def part_two(input_b:list, pairs:set, autocomplete_scores:set):
    total_score = []
    for inp in input_b:
        stack = deque()
        for ch in inp:
            if ch in pairs:
                stack.appendleft(pairs[ch])
            elif ch != stack.popleft():
                break
        else:
            score = 0
            for ch in stack:
                score = score * 5 + autocomplete_scores[ch]
            total_score.append(score)

    return sorted(total_score)[len(total_score)//2]



# print(part_one(input_brackets, pairs,syntax_error_scores))
print(part_two(input_brackets,pairs, autocomplete_scores))