def number_pyramid(n) :
    for i in range (1 , n+1) :
        print(' ' * (n - i)
              + ' '.join(str(j) for j in range(1, i+1)))

number_pyramid(5)

print('=============================================')

def right_angle_number_pyramid(n):
    for i in range(1, n+1):
        print(' '* (n-i), end = '')
        for j in range(1,i+1) :
            print(j , end = '')
        print('')
right_angle_number_pyramid(5)

print('=='*22)
def right_angle_number_pyramid(n):
    for i in range(1,n+1) :
        for j in range(1, i+1) :
            print(j , end = '')
        print('')
right_angle_number_pyramid(5)

print('===' * 20)


def inverted_pyramid(n):
    for i in range(n ,-1, -1 ):
        for j in range(0,i) :
            print(n , end='')
        print('\r')
inverted_pyramid(5)

print('==='*20)

def inverse_pyramid(n) :
    for i in range(n, -1 ,-1):
        print(n * (i-1))
inverse_pyramid(5)

print('==='*20)


def number_reverse(n):
    for i in range(1,n):                     # runs form i to n-1 , i.e 1 to 4
        for j in range(i , 0,-1) :           # this reverses the i loop iterations ,  if i= 2 then j will print 2 then print 1 .
            print(j , end='')
        print()
number_reverse(5)

