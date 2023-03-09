'''
9-Mar-2023
https://app.codility.com/c/run/trainingTFP6GX-P6H/

results:
https://app.codility.com/demo/results/trainingTFP6GX-P6H/
https://app.codility.com/demo/results/training8HXVE8-CR9/
'''

import random

def main():
    test_list = random.choice([
        [1,2,3,4,5],
        [-2,-4,-6,-8],
        [],
        [1,3,5,7,9,10,11,12,13,14,15]]
        )
    print(f'result: {cyclic_rotation(test_list, random.randint(0,100))}')

def cyclic_rotation(A, K):
    print(f'original list: {A}\nrotate {K} times to the right')
    if K == 0 or A == []:
        return A
    elif len(A) < K:
        shift = K % len(A)
        return A[-shift:] + A[: -shift]
    else:
        return A[-K:] + A[: -K]
    
if __name__ == "__main__":
    main() 