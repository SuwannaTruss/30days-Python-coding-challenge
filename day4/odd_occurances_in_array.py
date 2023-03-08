'''
8-Mar-2023
https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/

https://app.codility.com/demo/results/trainingXVGM73-96E/
'''

def main():
    test_list = (
        [9, 3, 9, 3, 9, 7, 9],
        [9, 3, 9, 3, 9, 7, 9, 7, 99]
        )
    for arr in test_list:
        print(odd_occurance(arr))

def odd_occurance(A):
    A.sort()
    i=0
    while i < len(A)-1:
        if A[i] == A[i+1]:
            i += 2
        else: 
            return A[i]
    return A[i]

if __name__ == "__main__":
    main() 