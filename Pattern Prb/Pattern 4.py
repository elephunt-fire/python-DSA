def diamond_pyramid (n) :
    for i in range(n) :
        print(' ' * (n-i-1) , '*' * (2*i+1))
    for i in range(n-2 , -1 ,-1) :
        print(' ' * (n-i-1) , '*'*(2*i+1))
diamond_pyramid(3)



# Loop 1
# i =0 , n=3 , n-i-1 =2 (2 empty spaces) 2*i+1 = 1 (1 star)
# i =1 , n=3 , n-i-1 = 1 (1 empty spaces) 2*i+1 = 3 (3 stars)
# i = 2 , n=3  , n-i-1 = 0 (0 empty space) 2*i+1 = 5 (5 stars)
# Loop 2
# n-2 = i = 1 , n=3  , n-i-1= 1 ( empty space) , 2*i+1 = 3 (3 stars)
# n-2 = i = 0 , n =3  , n-i-1 = 3 (empty spaces) , 2*i+1 = 1 (1 star)

print('='* 10)
# A kite
def diamond_pyramid1 (n) :
    for i in range(n) :
        print(' ' * (n-i-1) , '*' * (2*i+1))
    for i in range(n-1 , -1 ,-1) :
        print(' ' * (n-i-1) , '*'*(2*i+1))
diamond_pyramid1(3)

print('=' * 15)

# A half kite
def diamond_pyramid2 (n) :
    for i in range(n) :
        print(' ' * (n-i-1) , '*' * (i+1))
    for i in range(n-2 , -1 ,-1) :
        print(' ' * (n-i-1) , '*'*(i+1))
diamond_pyramid2(3)