'''
12-Mar-2023
Instruction:
https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/

Results:
https://app.codility.com/demo/results/training93EDD8-XVS/
https://app.codility.com/demo/results/training24ZDEB-RD4/
https://app.codility.com/demo/results/trainingYGMKET-VQK/

'''

def main():
    test_input = [
        [5, [3,4,4,6,1,4,4]],
        [4, [3,4,4,6,1,4,4]],
        [6, [3,4,4,6,1,4,4,7]]  
    ]
    for i in range(len(test_input)):
        print(f'X = {test_input[i][0]}, Array = {test_input[i][1]}')
        print(f'result: {solution(test_input[i][0], test_input[i][1])}')
        
def solution(N, A):
    counters = [0] * N
    max_count = 0
    last_update = 0

    for x in A:
        if  x <= N:
            counters[x-1] = max(counters[x-1], last_update)
            counters[x-1] += 1
            max_count = max(counters[x-1], max_count)
        else:
            last_update = max_count
    
    return [last_update if n < last_update else n for n in counters]

if __name__ == "__main__":
    main() 