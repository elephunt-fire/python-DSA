def inverted_right_pyramid (n) :
    for i in range (n-1 , -1, -1) :
        print(' ' * (n-i-1) , '*' * (i+1))

inverted_right_pyramid(3)

# n= 3 , i =2 n-i-1 = 3-2-1 = 0 (empty spaces) i+1 = 2+1 = 3 (3 stars)
# =>***
# n =3 , i = 1 n-i-1 = 3-1-1 = 1 (1 empty space) i+1 = 1+1 = 2 (2 stars)
# => **
# n =3  i = 0  n-i-1 = 3-0-1 = 2 (2 empty spaces) i+1 = 0+1 = 1 (1 star)
# =>  *


# NO empty spaces
def inverted_right_pyramid1 (n) :
    for i in range (n-1 , -1, -1) :
        print('*' * (i+1))
inverted_right_pyramid1(3)

print('==='*17)
