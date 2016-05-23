'''
    generate all subsets of a set of N elements.
    1) those that contain A and
    2) those that do not
'''

def subsets(pre, other):
    if len(other) == 0:
        valueList.append(pre[:])
    else:
        subsets(pre, other[1:])
        pre.append(other[0])
        subsets(pre, other[1:])
        pre.pop()


def subsets2(start, candi):
    valueList.append(candi)

    for i in range(start, len(S)):
        subsets2(i+1, candi+[S[i]])


valueList = []
candi = []
S = [1,2,3]
subsets2(0, [])
print valueList