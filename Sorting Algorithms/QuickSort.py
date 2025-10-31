"""
FUNCTION QuickSort(list)
    IF list has 1 or fewer elements
        RETURN list  // Base case: A list with 0 or 1 elements is already sorted.

    // Step 1: Choose a pivot (e.g., the last element of the list)
    SET pivot = last element of list

    // Step 2: Partition the list into two sublists
    SET left = []  // Elements less than or equal to pivot
    SET right = [] // Elements greater than pivot

    FOR each element in list (excluding pivot)
        IF element <= pivot
            ADD element to left
        ELSE
            ADD element to right

    // Step 3: Recursively sort the left and right sublists
    SET sorted_left = QuickSort(left)
    SET sorted_right = QuickSort(right)

    // Step 4: Combine sorted sublists and pivot
    RETURN sorted_left + [pivot] + sorted_right
END FUNCTION

"""
nums = [3,6,8,10,1,2,1]
def quickSort(list):
    if len(list) <= 1:
        return  list
    pivot = list[-1]

    left , right = [] , []
    for i in range(len(list) -1 ):
        if list[i] <= pivot :
            left.append(list[i])
        else :
            right.append(list[i])
    sort_left = quickSort(left)
    sort_right = quickSort(right)

    return sort_left+ [pivot] + sort_right

result = quickSort(nums)
print(result)