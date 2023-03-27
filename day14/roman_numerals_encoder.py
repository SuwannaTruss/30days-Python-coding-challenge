'''
27-Mar-2023
Instruction:
https://www.codewars.com/kata/51b62bf6a9c58071c600001b/train/python
'''

def main():
    test_input = [1, 4, 6, 14, 21, 89, 91, 984, 1000, 1889, 1989, 2023, 4999]
    for i in range(len(test_input)):
        print(f'number: {test_input[i]}')
        print(f'Roman numerals: {solution(test_input[i])}')

def solution(n):
    remainder = n
    quotient = 0
    result = ''
    symbols = [(1000, "M"), (900, "CM"), 
               (500, "D"), (400, "CD"),
               (100, "C"), (90, "XC"),
               (50, "L"), (40, "XL"),
               (10, "X"), (9, "IX"),
               (5, "V"), (4, "IV"), (1, "I")]

    for i in range(len(symbols)):
        if remainder <= 0:
            return result
        else:
            quotient = remainder // symbols[i][0]
            result = result + (symbols[i][1] * quotient) if quotient > 0 else result
            remainder = remainder % symbols[i][0]          
    return result

if __name__ == "__main__":
    main()