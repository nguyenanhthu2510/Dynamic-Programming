"""
    Space optimize solution
    Implementation of LCS problem
"""

str1 = "AGGTABZ"
str2 = "AGGTAB"

m = len(str1)
n = len(str2)

L = [[0 for i in range(n + 1)] for j in range(2)]

# binary index, used to index current row and previous row
bi = bool


def printSOS_Lcs(a):
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=" ")
        print()


def sosLCS():
    for i in range(m+1):
        # Compute current binary index
        bi = i & 1
        print('bi =', bi)
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[bi][j] = 0

            elif str1[i-1] == str2[j - 1]:
                L[bi][j] = L[1 - bi][j - 1] + 1

            else:
                L[bi][j] = max(L[1 - bi][j],
                               L[bi][j - 1])
        printSOS_Lcs(L)
        print("-------------------")
    print('Bang ket qua cuoi cung cua thuat toan la:')
    printSOS_Lcs(L)


print("Bang ban dau nhu sau:")
printSOS_Lcs(L)
print("\nThuc hien phep toi uu hoa khong gian cua LCS")
sosLCS()