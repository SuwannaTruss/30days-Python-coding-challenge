'''
14-Mar-2023
Instruction:
https://www.codewars.com/kata/5277c8a221e209d3f6000b56
'''

def main():
    test_input = ["(){}[]", "([{}])", "(}", "[(])", "[({})](]"]
    for i in range(len(test_input)):
        print(f'input string: {test_input[i]}')
        print(f'result: {valid_braces(test_input[i])}')

def valid_braces(string):
    closes = []
    for c in string:
        match c:
            case "(":
                closes.append(")")
            case "[":
                closes.append("]")
            case "{":
                closes.append("}")
            case _:
                if closes != [] and c == closes[-1]:
                    closes.pop()
                else:
                    return False
    if closes == []:
        return True
    else:
        return False
    
if __name__ == "__main__":
    main() 