#Goal: Sort an array called "nums" which has n integers: num[0...n-1]
#Insertion sort

def insertionSort(nums):
    for i in range(len(nums)):
        j = i - 1
        curr = nums[i]
        while j>=0 and nums[j] > curr:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = curr
    return nums

# print(insertionSort(nums = [3,4,1,6,8,11,2,9,1]))