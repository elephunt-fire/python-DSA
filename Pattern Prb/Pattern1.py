def pyramid(n):
    for i in range(n):
        print(' ' * (n-i-1) , '*'*(2*i+1))
pyramid(3)

# i = 0, n = 3 n-i-1 = 3-0-1  =2 (2 empty spaces) and 2*0+1 = 1 (1 star)
#  *
# i=1 , n=3  n-i-1 = 3-1-1 = 1 (1 empty space) and  2*1+1 = 3 (3 stars)
# ***
# i = 2 , n= 3  n-i-1 = 0 (no empty space) and 2*i+1 = 2*2+1 = 5 (5 stars)
#*****

print(('======================================'))
def reverse_pyramid(n) :
    for i in range(n-1 ,-1, -1) :
        print(' '*(n-i-1) ,'*' * (2*i+1))
reverse_pyramid(3)