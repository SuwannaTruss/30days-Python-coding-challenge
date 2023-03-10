'''
10-Mar-2023 (alternative solution)
Lesson 1: Iterations
https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

result:
https://app.codility.com/demo/results/trainingHFYRJD-NEH/
'''

def main():
    int_list = ([12, 23, 45, 67, 65, 43, 1041, 32, 2000000])
    for n in int_list:
        print(f'interger: {n}, the largest binary gap: {binary_gap(n)}.')

def binary_gap(N):
    binary = format(N, 'b')
    head = binary.find("1")
    tail = binary.find("1", head+1)
    max_gap = 0
    gap = 0
    while tail != -1:
        gap = tail - head - 1
        head = tail
        tail = binary.find("1", head+1)
        if gap > max_gap:
            max_gap = gap
    return max_gap


if __name__ == "__main__":
    main() 