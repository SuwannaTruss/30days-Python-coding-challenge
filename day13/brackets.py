'''
20-Mar-2023
Instruction:
https://app.codility.com/programmers/lessons/7-stacks_and_queues/brackets/

result:
https://app.codility.com/demo/results/trainingPYMDZD-V4K/
Note: Python earlier than 3.10 do not have "match case"
'''

def main():
    test_input = ["{[()()]}", "([)()]","(){}[]", "([{}])", "(}", "[(])", "[({})](]"]
    for i in range(len(test_input)):
        print(f'input string: {test_input[i]}')
        print(f'result: {solution(test_input[i])}')

def solution(S):
    brackets = {
        "(": ")",
        "{": "}",
        "[": "]"
    }
    closes = []

    for c in S:
        if c in brackets.keys():
            closes.append(brackets[c])
        elif len(closes) and closes[-1] == c:
            closes.pop()
        else:
            return 0
    return 0 if len(closes) else 1
    
if __name__ == "__main__":
    main() 