'''
10-Mar-2023
Instruction:
https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/

results:
https://app.codility.com/demo/results/trainingC5US5E-NPC/
https://app.codility.com/demo/results/training8QBT5N-2UC/

tips:
Gauss (Sum of sequence): https://dev.to/alisabaj/the-gauss-sum-and-solving-for-the-missing-number-996
sum() in python: https://www.geeksforgeeks.org/sum-function-python/
'''

import random

def main():
    test_array = random.choice([
        [2,1,3,5],
        [],
        [1],
        [2],
        [7,4,6,2,5,3]    
    ])
    print(f'missing number: {solution(test_array)}')

def solution(A):
    print(f'test_array: {A}')
    # find sum of sequence [1...(N)] using Gauss method
    guass_sum = ((len(A)+1) * (len(A)+2))//2
    A_sum = sum(A)
    return abs(A_sum - guass_sum)

if __name__ == "__main__":
    main() 