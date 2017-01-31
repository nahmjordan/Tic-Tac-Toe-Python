#function to check for winner
def check(isx, tl, tm, tr, ml, mm, mr, bl, bm, br):

    if (isx == True):
        win = 'X'
    else:
        win = 'O'

    if (tl == tm == tr == win or ml == mm == mr == win or bl == bm == br == win):
        print "\n %s is winner! \n" %win
        return True
    elif (tl == ml == bl == win or tm == mm == bm == win or tr == mr == br == win):
        print "\n %s is winner! \n" %win
        return True
    elif (tl == mm == br == win or tr == mm == bl == win):
        print "\n %s is winner! \n" %win
        return True
    else:
        return False

#function to print out game board
def gameboard():
    linebreak = "/////////////"

    print " " + gb['tl'] + " // " + gb['tm'] + " // " + gb['tr']
    print linebreak
    print " " + gb['ml'] + " // " + gb['mm'] + " // " + gb['mr']
    print linebreak
    print " " + gb['bl'] + " // " + gb['bm'] + " // " + gb['br']

instruct = "Enter either tl, tm, tr, ml, mm, mr, bl, bm, or br \n"
xturn = True
gb = {'tl': ' ', 'tm': ' ', 'tr': ' ', 'ml': ' ', 'mm': ' ', 'mr': ' ',
 'bl': ' ', 'bm': ' ', 'br': ' '}

#l1 = " " + gb['tl'] + " // " + gb['tm'] + " // " + gb['tr']
#l2 = " " + gb['ml'] + " // " + gb['mm'] + " // " + gb['mr']
#l3 = " " + gb['bl'] + " // " + gb['bm'] + " // " + gb['br']

print "\n\tTic-Tac-Toe!\n\n X goes first, \n"

#print out game board
gameboard()
print "\n"

for turns in range(1,10):

    choice = "blank"

    while choice not in gb or gb[choice] != " ":
        choice = raw_input(instruct)

    if xturn:
        gb[choice] = "X"
    else:
        gb[choice] = "O"

    gameboard()
    if check(xturn, **gb):
        break

    xturn = not xturn
