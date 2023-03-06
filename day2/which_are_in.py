'''
Day 2: 06-Mar-2023

https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/python

Instructions:
Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order of the strings of a1 which are substrings of strings of a2.

Example 1:
a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]

Example 2:
a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []

Notes:
Arrays are written in "general" notation. See "Your Test Cases" for examples in your language.
In Shell bash a1 and a2 are strings. The return is a string where words are separated by commas.
Beware: In some languages r must be without duplicates.
'''

def main():
    arr1 = ["arp", "live", "strong"]
    arr2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    print(in_array(arr1, arr2))

def in_array(array1, array2):
    r = []
    for a1 in array1:
        for a2 in array2:
            if a1 in a2 and a1 not in r:
                r.append(a1)
    r.sort()
    return r

if __name__ == "__main__":
    main()  