player1 = input("Player 1, please state your name: ")
player2 = input("Player 2, how may I call you? ")


repeat = True
player = 1
lineCorrect = False
columnCorrect = False
gameboard = [[" "," "," "],[" "," "," "],[" "," "," "]]
currentPlayer = player1
currentSymbol = "X"


def table():
        print("----------")
        for line in gameboard:
            print("|", end = "")
            for position in line:
                print(position, "|", end = "")
            print("")
            print("----------")
        print("")

def turnchanger():
    global player
    global currentSymbol
    global currentPlayer

    if player == 1:
        player = 2
    elif player == 2:
        player = 1
    
    if player == 1:
        currentPlayer = player1
    else: currentPlayer = player2

    if player == 1:
        currentSymbol = "X"
    else: currentSymbol = "O"

def turn():
    global currentPlayer
    global currentSymbol
    global lineCorrect
    global columnCorrect
    global linePos
    global columnPos

#choose line
    print("Alright, " + currentPlayer + ", in which line would you like to make your first move?")
    lineChoice = input()
    lineInt = int(lineChoice)
    linePos = lineInt - 1

    if linePos < 0 or linePos > 2:
        print("Sorry, this line does not exist.")
        return
    else: lineCorrect = True


#choose column
    print("And in which position shall we place your " + currentSymbol + " ?")
    columnChoice = input()
    columnInt = int(columnChoice)
    columnPos = columnInt - 1

    if columnPos < 0 or columnPos > 2:
            print("Sorry, this position does not exist.")
            return
    else: columnCorrect = True


table()
while repeat:
    turn()
    if lineCorrect and columnCorrect == True:      
       gameboard[linePos][columnPos] = currentSymbol
    table()
    if lineCorrect and columnCorrect == True:
        turnchanger()
    else: print("Please choose another position for your '" + currentSymbol + "'.")
    lineCorrect = False
    columnCorrect = False
    