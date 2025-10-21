def floyd_triange(n):
    num = 1
    for i in range(1, n+1):
        for j in range(1, i+1) :
            print(num , end=' ')
            num+=1
        print()
floyd_triange(5)
print('==='*15)
def floyd_triange1(n) :
    num =1
    for i in range(1, n+1) :
        for j in range(1, i+1 ):
            print(num, end ='')
        print()
floyd_triange1(5)

print('==='*15)
def pascal_triangle (n):
    for i in range(n):
        print(' '*(n-i) , end='')
        num =1
        for j in range(i+1) :
            print(num , end=' ')
            num = num * (i-j) // (j+1)
        print()
pascal_triangle(5)

