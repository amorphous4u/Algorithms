#Goal: Sort an array called "nums" which has n integers: num[0...n-1]
#selection sort

nums = [3,4,6,8,1,2,9,1]

def selectionSort(nums):
    for i in range(len(nums)):
        minelementindex = i
        minelement = nums[i]
        for m in range(i+1, len(nums)):
            if nums[m] < minelement:
                minelement = nums[m]
                minelementindex = m
        nums[i], nums[minelementindex] = nums[minelementindex], nums[i]

    return nums

print(selectionSort(nums))