# A couple Blackjack-related functions -- hw1 updated to provide exceptions
# for some error cases

# card value element constants
ACE = 1
MAX_NUM_CARD = 10
JACK = 11
QUEEN = 12
KING = 13

# score-related constants
ALT_ACE_VALUE = 11
FACE_CARD_VALUE = 10
BLACKJACK = 21

# hand-related constants
CARDS_PER_HAND = 2

class TooFewCardsError(Exception):
    " Too few cards to complete the deal for all players "
    pass

def deal(deck, hands):
    '''
    divide cards among hands, which are represented as a tuple of lists
    '''
    deck.reverse()
    nhands = len(hands)
    if len(deck) < CARDS_PER_HAND * nhands:
        raise TooFewCardsError
    for card_index in range(CARDS_PER_HAND):
        for next_hand in range(nhands):
            hands[next_hand].append(deck.pop())
    return hands

def score(hand):
    '''
    compute and return score of hand for Blackjack
    '''
    total = 0
    aces = 0
    for card in hand:
        if card[0] == ACE:
            aces += 1
            total += ALT_ACE_VALUE
        elif MAX_NUM_CARD <= card[0] <= KING:
            total += 10
        else:
            total += card[0]
    while total > BLACKJACK:
        if aces <= 0:
            break
        else:
            total -= 10
            aces -= 1
    return total
