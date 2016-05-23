'''
    Implement c(n, k) using Pascal's Triangle
'''

def comb(n, k):
    if k == 0 or n == k:
        return 1
    else:
        return comb(n-1, k-1) + comb(n-1, k)

print comb(8, 6)