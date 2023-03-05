'''
Day 1: 05-Mar-2023

https://www.codewars.com/kata/550498447451fbbd7600041c/train/python

Instructions:
Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) 
that checks whether the two arrays have the "same" elements, with the 
same multiplicities (the multiplicity of a member is the number of times 
it appears). "Same" means, here, that the elements in b are the elements 
in a squared, regardless of the order.
'''


def main():
    arr1 = [121, 144, 19, 161, 19, 144, 19, 11]
    arr2 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
    print(comp(arr1, arr2))

# my solution
def comp(array1, array2):     
    # check for false where items in a, b contain None
    if not (array1 is not None and array2 is not None) or None in array1 or None in array2: 
        return False
    
    # check for false if two arrays does not have the same size.
    if len(array1) != len(array2):
        return False
    else:
        # check multiplicities
        array1_pow2 = list(map(lambda num: num ** 2, array1))
        array1_pow2.sort()
        array2.sort()
        for i in range(len(array1)):
            if array1_pow2[i] == array2[i]:
                continue
            else:
                return False
    return True

if __name__ == "__main__":
    main()  