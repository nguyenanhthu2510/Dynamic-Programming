def show(c):
    for i in range(len(c)):
        for j in range(len(c[i])):
            print(c[i][j], end='\t')
        print()


def path(a):
    c = [[0 for i in range(len(a[0]) + 1)] for i in range(len(a) + 1)]

    for i in range(1, len(c)):
        for j in range(1, len(c[0])):
            if i + 1 == len(c):
                c[i][j] = max(c[i - 1][j - 1], c[i][j - 1])
            else:
                c[i][j] = max(c[i-1][j-1], c[i][j-1], c[i+1][j-1]) + a[i-1][j-1]
    show(c)
    return c


def re(a):
    i = len(a)
    j = len(a[0])
    c = path(a)
    print("Path in numeric table is:")
    while j>0:
        print((i, j), end='\t')
        if i>0:
            k = c[i][j] - a[i-1][j-1]
            if c[i-1][j-1] == k:
                i -= 1
                j -= 1
            elif c[i][j-1] == k:
                j -= 1
            else:
                i -= 1
        else:
            j -= 1


a = [[9,9,9,2,6,1,6],
     [4,5,2,1,4,5,1],
     [2,3,9,8,1,3,4],
     [5,7,2,1,9,8,1],
     [9,8,2,1,4,7,6],
     [3,7,1,3,6,8,1]]

re(a)
