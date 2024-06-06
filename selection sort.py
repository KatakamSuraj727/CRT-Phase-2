def performselectionsort(nums):
    n=len(nums)
    fixthisindex = n-1
    while fixthisindex>0:
        maxeleindex=fixthisindex

        for index in range(fixthisindex):
            if nums[index]>nums[maxeleindex]:
                maxeleindex = index
        if maxeleindex != fixthisindex:
            temp=nums[maxeleindex]
            nums[maxeleindex]=nums[fixthisindex]
            nums[fixthisindex]=temp
        print(nums)
        fixthisindex -=1
nums=[10, 8, 2, 14, 12, 7]
print("before sorting:",nums)
result=performselectionsort(nums)


print("after sorting nums:",nums)


        