'''
13-Mar-2023
Instruction:
https://app.codility.com/programmers/lessons/4-counting_elements/missing_integer/

result:


'''

def main():
    test_input = [
        [1,3,4,4,1,2],
        [1,2,3],
        [-1,-3],
        [0],
        [-1,-2,-5],
        [-1,-5,0,4],
        [0,4,5],
        [0,1,2],
        [-1,0,1,2]
    ]
    for i in range(len(test_input)):
        print(f'Array = {test_input[i]}')
        print(f'result: {solution(test_input[i])}')

def solution(A):
    list_A = list(set([0 if k <= 0 else k for k in list(set(A))]))
    list_A.sort()
    n = len(list_A)

    # all elements in A is negative or zero, return 1
    if  n == 1 and list_A[0] == 0:
        return 1
    elif list_A[0] == 0:
        sequence = list(range(list_A[-1]+1))
    else:
        sequence = list(range(1, list_A[-1]+1))
    
    # compare list_A and sequence for missing smallest integer, if no missing integer, it will return the N+1
    if list_A == sequence:
        return list_A[-1]+1
    else:
        for i in range(len(sequence)):
            if sequence[i] == list_A[i]:
                continue
            else:
                return sequence[i]
            
if __name__ == "__main__":
    main() 