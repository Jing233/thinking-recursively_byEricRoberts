'''
    if you call listPermutations('ABBC'), ervey entry will appear twice.
    improve the implementation so that the list includes no duplicate entries
'''

def noDuplicateListPermutations(prefix, rest):
    if len(rest) == 0:
        valueList.append(prefix)
    else:
        noDuplicateListPermutations(prefix+rest[0], rest[1:])
        for i in range(1, len(rest)):
            if rest[i] != rest[i-1]:
                noDuplicateListPermutations(prefix+rest[i], rest[:i]+rest[i+1:])


valueList = []
noDuplicateListPermutations('', 'ABCCC')
print valueList