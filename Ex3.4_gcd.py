'''
    the greatest common divisor of x and y is the same as that of y and r,
    where r is the remainder of x divided by y.
'''

def gcd(x, y):
    if y > x:
        x, y = y, x

    if x % y == 0:
        return y
    else:
        return gcd(y, x%y)

print gcd(10,902)