'''
    take an array of strings representing a set of cards and returns the number of different combinations of cards
    in the array that sum to fifteen
    clubs, diamonds, hearts and spades
    jacks, queens and kings are 10,
    aces counting as 1
'''
def card2num(card):
    if card[0] == 'A':
        return 1
    elif card[0] in ['1', 'J', 'Q', 'K']:
        return 10
    elif '2' <= card[0] <= '9':
        return ord(card[0]) - ord('0')


def countFifteens(val, cards, candi):
    if val == 15:
        valueList.append(candi)
    else:
        for i in range(len(cards)):
            countFifteens(val+card2num(cards[i]), cards[i+1:], candi+[cards[i]])

valueList = []
hand = ['5H', 'QH', '4D', '6C', '10S']
countFifteens(0, hand, [])
print valueList