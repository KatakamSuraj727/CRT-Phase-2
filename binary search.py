nums=[11,12,4,5]
target=23
nums=sorted(nums)
left=0
right=len(nums)-1
flag=-1

while left <= right:
    mid=(left+right)//2
    if nums[mid]==target:
        flag=mid
        break
    elif nums[mid]>target:
        right=mid-1
    else:
        left=mid-1
if flag==-1:
    print("targrt noot found")
else:
    print("target is found")


