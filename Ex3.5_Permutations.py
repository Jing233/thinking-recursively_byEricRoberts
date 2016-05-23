'''
    determine the number of ways in which one can select an ordered set of
    k elements from a collection of n distinct objects.
'''

def permut(n, temp):
    if n == temp:
        return 1
    else:
        return n*permut(n-1, temp)
n = 7
k = 5
print permut(n, n - k)