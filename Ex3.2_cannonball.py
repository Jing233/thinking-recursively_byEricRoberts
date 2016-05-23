'''
    implement cannonball:
    1 + 2 + 4 + 8 + 2^(N-1) == 2^N - 1
'''

def cannonball(N):
    if N == 0:
        return 1
    else:
        return 2*cannonball(N-1)

result = 0


if __name__ == '__main__':
    N = int(raw_input("Enter the number of layers:"))
    for i in range(N):
        result += cannonball(i)
    print result