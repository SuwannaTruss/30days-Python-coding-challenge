'''
07-Mar-2023
Lesson 1: Iterations
https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

result:
https://app.codility.com/demo/results/training9RGDK3-42A/
'''

def main():
    int_list = ([12, 23, 45, 67, 65, 43, 1041, 32, 2000000])
    for n in int_list:
        print(f'interger: {n}, the largest binary gap: {binary_gap(n)}.')

def binary_gap(N):
    binary = format(N, 'b')
    head = tail = 0
    max_gap = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            head = i
            gap = head - tail - 1
            if gap > max_gap:
                max_gap = gap
            tail = head   
    return max_gap


if __name__ == "__main__":
    main() 