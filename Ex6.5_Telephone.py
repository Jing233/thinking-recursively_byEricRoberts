'''
    write a program that accepts a string of digits and prints all possible sequences
    of letters corresponding to that telephone number.
'''

def telletters(pre, rest):

    if len(rest) == 0:
        valueList.append(pre)

    else:
        for j in range(len(TeleDict[str(rest[0])])):
            telletters(pre+TeleDict[str(rest[0])][j], rest[1:])




TeleDict = {'0':['0'], '1':['1'], '2':['A', 'B', 'C'], '3':['D', 'E', 'F'], '4':['G', 'H', 'I'],
            '5':['J', 'K', 'L'], '6':['M', 'N', 'O'], '7':['P', 'R', 'S'], '8':['T', 'U', 'V'], '9':['W','X','Y']}

valueList = []
telletters('', '637100')
print len(valueList)