'''
11-Mar-2023
Instruction:
https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/

Result:
https://app.codility.com/demo/results/trainingBUF5C2-Z8Q/

'''


def solution(X, A):
    step = [0] * X
    for i in range(X):
        try:
            step[i] = A.index(i+1)
        except:
            return -1
    return max(step)

