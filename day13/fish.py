'''
20-Mar-2023
Instruction:
https://app.codility.com/programmers/lessons/7-stacks_and_queues/fish/

result:
https://app.codility.com/demo/results/training8G4UKF-7V8/
'''

def main():
    test_input = [
        [[4, 8, 2, 6, 7], [0, 1, 1, 0, 0]],
        [[4, 3, 2, 1, 5], [0, 1, 0, 0, 0]]
    ]
    for i in range(len(test_input)):
        print(f'Size: {test_input[i][0]}, Direction: {test_input[i][1]}')
        print(f'result: {solution(test_input[i][0], test_input[i][1])}')


def solution(A, B):
    survivors = 0
    downstream_fish = []

    for i in range(len(B)):
        if B[i] == 1:
            downstream_fish.append(A[i])
        else:
            while len(downstream_fish) and downstream_fish[-1] < A[i]:
                    downstream_fish.pop()
            if not len(downstream_fish):
                survivors += 1    
    return len(downstream_fish) + survivors

if __name__ == "__main__":
     main()