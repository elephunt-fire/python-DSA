def right_pyramid(n) :
    for i in range(n) :
        print('*'*(i+1))
right_pyramid(3)

# If there is a gap of 2 stars in occurance .
def right_pyramid1(n) :
    for i in range(n) :
        print('*'*(2*i+1))
right_pyramid1(3)



# i = 0 , n=3
# there are no empty spaces available in a right angle triangle. So only on formula needed.
# print '*' *(i+1) = 0+1 = 1   =>*
# i+1 = 1+1 = 2 =>**
# i+1 = 2+1 = 3 =>***
