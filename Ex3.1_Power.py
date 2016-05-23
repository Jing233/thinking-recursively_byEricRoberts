'''
    implement power(x, k), where x is a real value
    k is always a nonnegative integer
'''

def power(x, k):
    if k == 1:
        return x
    elif k == 0:
        return 1
    else:
        return x*power(x, k-1)


print power(0.9, 3)

