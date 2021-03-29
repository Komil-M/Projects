import random    # required for shuffle method of Deck

class Card(object):
    ''' Suit and rank are ints, and index into suit_list and rank_list.
        Value is different from rank: for example face cards are equal in value (all 10)
    '''
    # Use these lists to map the ints of suit and rank to nice words.
    # The 'x' is a place holder so that index-2 maps to '2', etc.
    suit_list = ['x','c','d','h','s']
    rank_list = ['x', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10','J', 'Q', 'K']

    def __init__(self, rank=0, suit=0):
        ''' Rank and suit must be ints. This checks that they are in the correct range.
            Blank card has rank and suit set to 0.
        '''
        if type(suit) == int and type(rank) == int:
            # only good indicies work
            if suit in range(1,5) and rank in range(1,15):
                self.__suit = suit
                self.__rank = rank

            else:
                self.__suit = 0
                self.__rank = 0
        else:
            self.__suit = 0
            self.__rank = 0
    def get_rank(self):
        return self.__rank

    def get_suit(self):
        return self.__suit
    
##    These two "set" methods are for testing: turn them on for testing and
##    and then turn off.  These allow you to change a card's rand and suit so
##    you can test situations that might occur infrequently.
##
##    def set_rank(self, rank):
##        self.__rank = rank
##
##    def set_suit(self, suit):
##        self.__suit = suit

    def get_value(self):
        ''' Face cards return 10, the rest return their rank values. Aces are low.
        '''
        # ternary expression:
        return self.__rank if self.__rank < 10 else 10

    def equal_suit(self, other):
        '''Returns True if suits are equal.'''
        return self.__suit == other.__suit

    def equal_rank(self, other):
        '''Returns True if ranks are equal.'''
        return self.__rank == other.__rank

    def equal_value(self, other):
        '''Returns True if values are equal.'''
        return self.get_value() == other.get_value()

    def __str__(self):
        ''' Called by print() so you can print a card, just like any other data structure.
        '''
        # Uses rank to index into rank_list of names; uses suite to index into suit_list of names.
        #print(self.__rank)
        return "{:s}{:s}".format((self.rank_list)[self.__rank], (self.suit_list)[self.__suit])

    def __repr__(self):
        ''' This method is called if you simply enter a card name in the shell.
            It simply calls, the same method that prints a card.
        '''
        return self.__str__()

class Deck(object):
    ''' Deck of cards, implemented as a list of card objects.
        The last card in the deck (list) is the top of deck.
    '''
    def __init__(self):
        self.__deck=[Card(rank,suit) for suit in range(1,5) for rank in range(1,14)]

    def shuffle(self):
        '''Shuffle the deck using a call to random.'''
        random.shuffle(self.__deck)

    def deal(self):
        '''Return the top card from the deck (only if the deck is not empty).'''
        # ternary expression
        return self.__deck.pop() if len(self.__deck) else None

    def cards_count(self):
        '''Returns the number of cards in the deck.'''
        return len(self.__deck)

    def is_empty(self):
        '''Returns True if the deck is empty.'''
        return len(self.__deck) == 0

    def __str__(self):
        ''' Print a deck, simple but messy!
        '''
        return ','.join([str(card) for card in self.__deck])
            
    def __repr__(self):
        ''' Messy print deck, if you enter a deck's name in the shell.
        '''
        return self.__str__()

myCard = Card()
myDeck = Deck()
myDeck.shuffle()

community = []
player1 = []
player2 = []

for i in range(5):
    community.append(myDeck.deal())
print(community)

for i in range(2):
    player1.append(myDeck.deal())
    player2.append(myDeck.deal())
print(player1)
print(player2)

player1.extend(community)
player2.extend(community)

print("Player 1 hand ",player1)
print("Player 2 hand ",player2)

myRanks = []
    
for i in range(len(player1)):
    myRanks.append(player1[i].get_rank())
        
for j in range(len(myRanks)):
    myRanks[j] = int(myRanks[j])    
myRanks.sort()
print(myRanks)

def straight(myList):
    myRanks = []
    
    for i in range(len(myList)):
        myRanks.append(myList[i].get_rank())
        
    for j in range(len(myRanks)):
        myRanks[j] = int(myRanks[j])
        
    myRanks.sort()
    for k in range(len(myRanks)-1):
        if (myRanks[k] == myRanks[k+1]-1 and myRanks[k+1] == myRanks[k+2]-1  and
           myRanks[k+2] == myRanks[k+3]-1  and myRanks[k+3] == myRanks[k+4]-1 and
           myRanks[k+4] == myRanks[k+5]-1):
            return True
        else:
            return False

def one_pair(myList):
    myRanks = []
    
    for i in range(len(myList)):
        myRanks.append(myList[i].get_rank())
        
    for j in range(len(myRanks)):
        myRanks[j] = int(myRanks[j])      
    myRanks.sort()
    for k in range(len(myRanks)-1):
        if (myRanks[k] == myRanks[k+1] or myRanks[k+1] == myRanks[k+2]  or
           myRanks[k+2] == myRanks[k+3]  or myRanks[k+3] == myRanks[k+4] or
           myRanks[k+4] == myRanks[k+5] or myRanks[k+5] == myRanks[k+6]):
            return True
        else:
            return False

def two_pair(myList):
    myRanks = []
    
    for i in range(len(myList)):
        myRanks.append(myList[i].get_rank())
        
    for j in range(len(myRanks)):
        myRanks[j] = int(myRanks[j])
    myRanks.sort()

    for k in range(len(myRanks)-1):
        if (myRanks[k] == myRanks[k+1] and myRanks[k+2] == myRanks[k+3] # 1st pair with the rest
            or
            myRanks[k] == myRanks[k+1] and myRanks[k+3] == myRanks[k+4]
            or
            myRanks[k] == myRanks[k+1] and myRanks[k+4] == myRanks[k+5]
            or
            myRanks[k] == myRanks[k+1] and myRanks[k+5] == myRanks[k+6]
            or
           myRanks[k+1] == myRanks[k+2]  and myRanks[k+3] == myRanks[k+4] #2nd pair with the rest
            or
            myRanks[k+1] == myRanks[k+2]  and myRanks[k+4] == myRanks[k+5]
            or
            myRanks[k+1] == myRanks[k+2]  and myRanks[k+5] == myRanks[k+6]
            or
           myRanks[k+2] == myRanks[k+3] and myRanks[k+4] == myRanks[k+5] #3rd pair with the rest
            or
            myRanks[k+2] == myRanks[k+3] and myRanks[k+5] == myRanks[k+6]
            or
            myRanks[k+3] == myRanks[k+4] and myRanks[k+5] == myRanks[k+6]):
            return True
        else:
            return False

def three_of_a_kind(myList):
    myRanks = []
    
    for i in range(len(myList)):
        myRanks.append(myList[i].get_rank())
        
    for j in range(len(myRanks)):
        myRanks[j] = int(myRanks[j])
    myRanks.sort()
    for k in range(len(myRanks)-1):
        if (myRanks[k] == myRanks[k+1] and myRanks[k] == myRanks[k+2]
            or
           myRanks[k+1] == myRanks[k+2]  and myRanks[k+1] == myRanks[k+3] 
            or
           myRanks[k+2] == myRanks[k+3] and myRanks[k+2] == myRanks[k+4] 
            or
            myRanks[k+3] == myRanks[k+4] and myRanks[k+3] == myRanks[k+5]
            or
            myRanks[k+4] == myRanks[k+5] and myRanks[k+4] == myRanks[k+6]):
            return True
        else:
            return False

def full_house(myList):
    myRanks = []
    
    for i in range(len(myList)):
        myRanks.append(myList[i].get_rank())
        
    for j in range(len(myRanks)):
        myRanks[j] = int(myRanks[j])
    myRanks.sort()
    
    for k in range(len(myRanks)-1):
        if ((myRanks[k] == myRanks[k+1] and myRanks[k] == myRanks[k+2]) #1st 3 of a kind
            and
            (myRanks[k+3] == myRanks[k+4] or myRanks[k+4] == myRanks[k+5] or myRanks[k+5] == myRanks[k+6]) #1st pair with rest
            or
            (myRanks[k+1] == myRanks[k+2] and myRanks[k+1] == myRanks[k+3])
            and
            (myRanks[k+4] == myRanks[k+5] or myRanks[k+5] == myRanks[k+6])): #2nd pair with rest
            return True
        else:
            return False

def four_of_a_kind(myList):
    myRanks = []
    
    for i in range(len(myList)):
        myRanks.append(myList[i].get_rank())
        
    for j in range(len(myRanks)):
        myRanks[j] = int(myRanks[j])
    myRanks.sort()
    for k in range(len(myRanks)-1):
        if (myRanks[k] == myRanks[k+1] and myRanks[k] == myRanks[k+2] and myRanks[k] == myRanks[k+3]
            or
           myRanks[k+1] == myRanks[k+2]  and myRanks[k+1] == myRanks[k+3] and myRanks[k+1] == myRanks[k+4]
            or
           myRanks[k+2] == myRanks[k+3] and myRanks[k+2] == myRanks[k+4] and myRanks[k+2] == myRanks[k+5]
            or
            myRanks[k+3] == myRanks[k+4] and myRanks[k+3] == myRanks[k+5] and myRanks[3] == myRanks[k+6]):
            return True
        else:
            return False

def flush(myList):
    mySuits = []
    
    for i in range(len(myList)):
        mySuits.append(myList[i].get_suit())
    for j in range(len(mySuits)):
        mySuits[j] = int(mySuits[j])
        
    mySuits.sort()
    for k in range(len(mySuits)-1):
        if (mySuits[k] == mySuits[k+1]-1 and mySuits[k+1] == mySuits[k+2]-1  and
           mySuits[k+2] == mySuits[k+3]-1  and mySuits[k+3] == mySuits[k+4]-1 and
           mySuits[k+4] == mySuits[k+5]-1):
            return True
        else:
            return False
        
def straight_flush(myList):
    if flush(myList) == True and straight(myList) == True:
        return True
    else:
        return False

print("Straight: ",straight(player1))
print("____________________")
print("One pair: ",one_pair(player1))
print("____________________")
print("Two pair: ",two_pair(player1))
print("____________________")
print("Three of a kind: ",three_of_a_kind(player1))
print("____________________")
print("Four of a kind: ",four_of_a_kind(player1))
print("____________________")
print("Full house: ",full_house(player1))
print("____________________")
print("flush: ",flush(player1))
print("____________________")
print("straight flush: ",straight_flush(player1))

"""
def decide(x):
    if two_pair(x) == True:
        print("Win with two pair")
    elif one_pair(x) == True:
        print("win with one pair")

decide(player1)
"""

def decide(x):
    if straight_flush(x) == True:
        z = "wins with Straight Flush: "
        win_type = 1
        return win_type, z
    elif four_of_a_kind(x) == True:
        z = "wins with Four of a kind: "
        win_type = 2
        return win_type, z
    elif full_house(x) == True:
        z = "wins with Full house: "
        win_type = 3
        return win_type, z
    elif flush(x) == True:
        z = "wins with Flush: "
        win_type = 4
        return win_type, z
    elif straight(x) == True:
        z = "wins with Straight: "
        win_type = 5
        return win_type, z
    elif three_of_a_kind(x) == True:
        z = "wins with three of a kind: "
        win_type = 6
        return win_type, z
    elif two_pair(x) == True:
        win_type = 7
        z = "wins with two pair: "
        return win_type, z
    elif one_pair(x) == True:
        win_type = 8
        z = "wins with one pair: "
        return win_type, z
    else:
        win_type = 9
        z = "wins with highest card: "
        return win_type, z

print("########################################")

print("Player 1 ",decide(player1))
print("Player 2 ",decide(player2))

print("########################################")

if decide(player1) > decide(player2):
    print("Final winner: Player 2" ,decide(player2))
elif decide(player1) < decide(player2):
    print("Final winner: Player 1" ,decide(player1))
else:
    print("Draw")


    

        
        


"""
def one_pair(myList):
    myRanks = []
    
    for i in range(len(myList)):
        myRanks.append(myList[i].get_rank())
        
    for j in range(len(myRanks)):
        myRanks[j] = int(myRanks[j])
    count = 0
    temp = 20
    myRanks.sort()
    print(myRanks)
    for k in range(len(myRanks)-1):
        if myRanks[k] == myRanks[k+1]:
            return True
        else:
            return False

def one_pairF(myList):
    myRanks = []
    
    for i in range(len(myList)):
        myRanks.append(myList[i].get_rank())
        
    for j in range(len(myRanks)):
        myRanks[j] = int(myRanks[j])
    count = 0
    temp = 20
    myRanks.sort()
    print(myRanks)
    for k in range(len(myRanks)-1):
        if myRanks[k] != myRanks[k+1]:
            continue
        else:
            return True
            

if one_pair(player1) == False:
   print (one_pairF(player1))
else:
    print(one_pair(player1))
"""

    



