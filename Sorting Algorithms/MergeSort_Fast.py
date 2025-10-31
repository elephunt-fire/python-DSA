nums = [38, 27, 43, 3, 9, 82, 10]
def mergeSort(nums):
    n = len(nums)
    if n <=1 :
        return nums

    left = mergeSort(nums[:n//2])
    right = mergeSort(nums[n//2:])

    return running(left, right)

def running(left, right):
    res = []
    i,j = 0,0

    while i<len(left) and j< len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.append(right[j:])
    return res

result = mergeSort(nums)
print(result)