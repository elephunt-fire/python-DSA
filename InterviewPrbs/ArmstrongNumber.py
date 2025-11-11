def is_armstong(n):
    n_str = str(n)
    n_terms = len(n_str)
    sum = 0
    for i in n_str:
        sum +=  int(i) ** n_terms
    return sum == n

print(is_armstong(9474))

def armstrong_in_range(start,end):
    armsstrong_nums = []
    for i in range(start, end+1):
        if is_armstong(i):
            armsstrong_nums.append(i)
    return armsstrong_nums
print(armstrong_in_range(1,1000))
