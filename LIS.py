# memo table
def lis(a):
    table = [0 for i in range(len(a) + 1)]
    table[1] = 1
    for i in range(2, len(table)):
        if a[i - 2] < a[i - 1]:
            table[i] = max(table) + 1
        else:
            table[i] = table[i - 1] - 1
    print('memo table', table)
    return table


# back trace
def back_trace(a):
    table = lis(a)
    maxIndex = table.index(max(table))
    print('back trace:', end=' ')
    print(a[maxIndex-1], end=' ')
    while maxIndex-1 > 0:
        m = table.index(max(table[:maxIndex]))
        if m != maxIndex:
            print(a[m-1], end=' ')
        maxIndex = m


num = '25463897'
print('string number', num)
back_trace(num)

