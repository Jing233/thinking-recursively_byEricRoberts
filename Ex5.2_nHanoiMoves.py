'''
    nHanoiMoves(n) returns the number of moves required to solve the Tower of Hanoi Puzzle
    for a Tower of size n
'''

def nHanoiMoves(n):
    if n == 1:
        return 1
    else:
        return 2*nHanoiMoves(n-1)+1

print nHanoiMoves(8)