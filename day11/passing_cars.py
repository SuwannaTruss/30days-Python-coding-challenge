'''
Instruction:
https://app.codility.com/programmers/lessons/5-prefix_sums/passing_cars/

Result:
https://app.codility.com/demo/results/training4V3VJV-WKQ/
https://app.codility.com/demo/results/training34JUKW-U3N/
'''

def main():
    test_input = [
        [0,1,0,1,1],
        [0],
        [1],
        [0,0],
        [1,1],
        [0,1,0],
        [1,0,1],
        [1,1,0]
    ]
    for i in range(len(test_input)):
        print(f'Array = {test_input[i]}')
        print(f'result: {solution(test_input[i])}')

def solution(A):
    count = 0
    suffix_sum = [0] * (len(A)+1)
    for i in reversed(range(len(A))):
        suffix_sum[i] = A[i]+ suffix_sum[i+1]
        if A[i] == 0:
            count += suffix_sum[i]  
        if count > 1000000000:
            return -1     
    return count

if __name__ == "__main__":
    main() 
