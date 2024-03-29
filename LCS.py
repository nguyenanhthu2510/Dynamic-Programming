"""
    LCS - Longest Common Subsequence
"""

# from pip._vendor.msgpack.fallback import xrange

str1 = "AG"
str2 = "AGB"

m = len(str1)
n = len(str2)

# L = [[None]*(n+1) for i in xrange(m+1)]   the same like the following code
L = [[None for i in range(n + 1)] for i in range(m + 1)]


# print(L)


def lcs():
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                L[i][j] = 1 + L[i - 1][j - 1]
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])
            print(L[i][j], end=" ")
        print()
    # the result is in the last position of 2D array


def printLcs():
    # Following code is used to print LCS
    index = L[m][n]

    # Create a character array to store the lcs string
    lcs = [""] * (index + 1)
    lcs[index] = ""

    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    i = m
    j = n
    while i > 0 and j > 0:
        # If current character in X and Y are same, then
        # current character is part of LCS
        if str1[i - 1] == str2[j - 1]:
            lcs[index - 1] = str1[i - 1]
            i -= 1
            j -= 1
            index -= 1

        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif L[i - 1][j] > L[i][j - 1]:
            i -= 1
        else:
            j -= 1

    print("LCS of " + str1 + " and " + str2 + " is " + "".join(lcs))


lcs()
printLcs()

