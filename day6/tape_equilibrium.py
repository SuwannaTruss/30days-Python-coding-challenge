'''
10-Mar-2023
Instruction:


results:
https://app.codility.com/demo/results/training9K4QJZ-WJW/
https://app.codility.com/demo/results/training8EDSBN-VCY/
https://app.codility.com/demo/results/training76JM4R-6SZ/
'''

import random

def main():
    test_array = random.choice([
        [3,1,2,4,3],
        [-1000, 1000],
        [5, -5],
        [0,0],
        [7,4,6,2,5,3]    
    ])
    print(f'result: {solution(test_array)}')

def solution(A):
    print(f'input: {A}')
    min = 100000
    total = sum(A)
    cum = 0

    for n in A[:-1]:
        cum += n
        diff = abs(total - 2*cum)
        if (diff < min):
            min = diff
    return min

if __name__ == "__main__":
    main() 