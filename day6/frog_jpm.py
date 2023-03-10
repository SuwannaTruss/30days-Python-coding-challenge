'''
instruction:
https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/

result:
https://app.codility.com/demo/results/trainingNAYKR7-3VD/
'''

import math
import random

def main():
    start = random.randint(1, 1000000000)
    target = start + random.randint(1, 1000000000)
    jump = random.randint(1, 1000000000)
    print(f'start: {start}, target: {target}, jump: {jump}')
    print(f' No of jump to target: {frogJmp(start, target, jump)}')

def frogJmp(X, Y, D):
    return math.ceil((Y-X)/D)

if __name__ == "__main__":
    main() 