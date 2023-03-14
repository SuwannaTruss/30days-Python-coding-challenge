
#problem found on leet code
#binary search problem

def binary_search(nums,target):
    l,r=0,len(nums)-1
    while(l<=r):
        m=l+(r-l)//2
        if nums[m]==target:
            return m
        elif nums[m]>target:
            r=m-1
        else:
            l=m+1
    return -1




def main():
    nums = [-1,0,3,3,5,9,12]
    target = 3
    print(binary_search(nums,target))
    #print(search(nums,target))



if __name__=="__main__":
    main()