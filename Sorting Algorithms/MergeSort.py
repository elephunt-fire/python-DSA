nums = [38, 27, 43, 3, 9, 82, 10]
def mergeSort(list):
    if len(list) <= 1 :
        return list
    mid = len(list) //2
    left = list[mid:]
    right = list[:mid]

    sort_left = mergeSort(left)
    sort_right = mergeSort(right)

    return merge(sort_left,sort_right)

def merge(left ,right):
    result = []
    i,j= 0,0
    while i < len(left) and j < len(right):
        if left[i] <= right[j] :
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    print(left , "\t", right)

    while i< len(left) :
        result.append(left[i])
        i+=1

    while j < len(right):
        result.append(right[j])
        j+=1
    return  result

sort_list = mergeSort(nums)
print(sort_list)