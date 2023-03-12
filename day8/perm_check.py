'''
12-Mar-2023
Instruction:
https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

result:
https://app.codility.com/demo/results/trainingBUP3P6-U8Q/
https://app.codility.com/demo/results/trainingB2BTWZ-RWQ/
'''

def main():
    test_input = [
        [4,1,3,2],
        [4,1,3],
        [4,1,3,2,6,5],  
        [4,6,5],
        [1,2,2,3],
        [2,3,4]
    ]
    for i in range(len(test_input)):
        print(f'Array = {test_input[i]}')
        print(f'result: {solution(test_input[i])}')

def solution(A):
    n = len(A)
    n_set = len(set(A))
    lowest = min(A)
    highest = max(A)

    if n != n_set or n != highest-lowest+1:
        return 0
    else:
        sum_A = sum(A)
        gauss_sum = (n * (n+1))//2
    return int(sum_A == gauss_sum)

if __name__ == "__main__":
    main() 