'''
    implement square using the recurrence relation between (N+1)^2 and N^2
'''

def square(N):
    if N == 0:
        return 0
    else:
        return square(N-1) + 2*N - 1

N = int(raw_input('Enter the N:'))
print square(N)