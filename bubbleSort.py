#Goal: Sort an array called "nums" which has n integers: num[0...n-1]
#Bubble sort

nums = [3,4,1,6,8,11,2,9,1]

def bubbleSort(nums):
    for i in range(len(nums)):
        for m in range(len(nums)-1, i, -1):
            if nums[m] < nums[m-1]:
                nums[m-1],nums[m] = nums[m], nums[m-1]
    return nums

print(bubbleSort(nums))