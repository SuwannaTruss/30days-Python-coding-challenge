def main():
    #nums = [1,3,-1,-3,5,3,6,7]
    nums=[2,4,7]
    k=2
    #k = 3

    max_sliding(nums,k)

def max_sliding(nums,k):
    result=[]
    max_value=max(nums[0:k])
    max_index=nums.index(max_value)
    result.append(max_value)
    left=0
    for left in range(1,len(nums)-k+1):
        right=left+k-1
        incoming_value=nums[right]
        if(max_index<left):
            max_value=max(nums[left:right+1])
        else:
            max_value=max(max_value,incoming_value)
        print(left,right,max_value)
        max_index=nums.index(max_value)
        result.append(max_value)
    print(result)


    


if __name__=="__main__":
    main()