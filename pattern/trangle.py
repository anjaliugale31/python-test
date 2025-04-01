def trangle(t):
    for i in range(t):
        for j in range(i):
            print(j, end=' ')
        print()
 
# trangle(9)


def trangle1(t):
    for i in range(t):
        for j in range(t-i):
            print(j, end=' ')
        print()
 
# trangle1(9)

def tr(t):
    for i in range(t):
        for j in range(t-i-1):
            print(' ', end=' ')
        for k in range(i+1):
            print(k, end=' ')

        print()
tr(5)