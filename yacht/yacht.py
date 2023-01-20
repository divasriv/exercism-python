# Score categories.
# Change the values as you see fit.
YACHT = 'YACHT'
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 'FULL HOUSE'
FOUR_OF_A_KIND = 'FOUR OF A KIND'
LITTLE_STRAIGHT = 'LITTLE STRAIGHT'
BIG_STRAIGHT = 'BIG STRAIGHT'
CHOICE = 'CHOICE'

NUMBERS=[ONES, TWOS, THREES, FOURS, FIVES, SIXES]

def score(dice, category):

    dice.sort() 
    if category in NUMBERS:
        return dice.count(category) * category
    if category==CHOICE:
        return sum(dice)
    if category==LITTLE_STRAIGHT:
        if(dice==[1,2,3,4,5]): #no matter what order, dice.sort will bring it back to this order
            return 30
    if category==BIG_STRAIGHT:
        if(dice==[2,3,4,5,6]):
            return 30
    if category==YACHT:
        if len(set(dice))==1: #all digits are equal, so set size becomes 1
            return 50
    if category==FULL_HOUSE:
        if len(set(dice))==2: #after sort, dice=[a,a,b,b,b] or [a,a,a,b,b], set size is 2
            if dice[1]!=dice[3]: #whether dice is [a,a,b,b,b] or [a,a,a,b,b] dice[1] and dice[3] will always be different
                return sum(dice)
    if category==FOUR_OF_A_KIND: #after sort, dice=[a,b,b,b,b] or[a,a,a,a,b], counting occurance of dice[0] or dice[1] is enough
        if dice.count(dice[0])>=4:
            return dice[0]*4
        if dice.count(dice[1])>=4:
            return dice[1]*4
    return 0 #if all fails, return 0



