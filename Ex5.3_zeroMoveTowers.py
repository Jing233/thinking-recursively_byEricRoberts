'''
    Implement MoveTower with zero base case rather than one as its simple case.
'''

def zeroMoveTower(n, start, finish, temp):
    if n > 0:
        zeroMoveTower(n-1, start, temp, finish)
        print start,'-->',finish
        zeroMoveTower(n-1,temp, finish, start)



zeroMoveTower(3, 'A', 'B', 'C')