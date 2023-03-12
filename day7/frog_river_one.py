'''
11-Mar-2023
Instruction:
https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/

Result:
https://app.codility.com/demo/results/trainingBUF5C2-Z8Q/
https://app.codility.com/demo/results/trainingM35SQM-88Q/
'''

def main():
    test_input = [
        [5, [1,3,1,4,2,3,5,4]],
        [6, [1,3,1,4,2,3,5,4]],
        [6, [3,4,2,3,5,4,6]]  
    ]
    for i in range(len(test_input)):
        print(f'X = {test_input[i][0]}, Array = {test_input[i][1]}')
        print(f'result: {solution(test_input[i][0], test_input[i][1])}')

def solution(X, A):
    n = len(A)
    steps = [0] * (X+1)
    count = 0

    for i in range(n):
        if steps[A[i]] == 0:
            steps[A[i]] += 1
            count += 1
        else:
            continue
        if count == X:
            return i
    return -1

if __name__ == "__main__":
    main() 