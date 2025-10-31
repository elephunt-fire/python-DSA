nums = [38, 27, 43, 3, 9, 82, 10]
def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1] :
                nums[j] , nums[j+1] = nums[j+1] , nums[j]
    return nums

result = bubbleSort(nums)
print(result)