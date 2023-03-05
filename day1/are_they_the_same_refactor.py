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
# refactor 
# - using list comprehension and sorted i/o map() and sort() 
#   to shorten the code and no need to define variable that will not be used again int he code.
# - using of Try and Except, this will capture 
#      a) TypeError: None Type Object Is Not Iterable (ie. array1 = None)
#      b) TypeError: unsupported operand type(s) for **: 'int' and None

def comp(array1, array2):   
    try:
        return sorted([num ** 2 for num in array1]) == sorted(array2)
    except:
        return False

if __name__ == "__main__":
    main() 