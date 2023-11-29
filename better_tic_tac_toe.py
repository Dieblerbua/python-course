player1 = input("Player 1, please state your name: ")
player2 = input("Player 2, how may I call you? ")

repeat = True
player = 1
lineCorrect = False
columnCorrect = False
emptySpace = False
win = False
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
    global player1
    global player2

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
    global emptySpace

#choose line
    print(currentPlayer + ", in which line would you like to make your first move?")
    lineChoice = input()
    if lineChoice.isdigit() == False:
        print("This is not a number.")
        return
    lineInt = int(lineChoice)
    linePos = lineInt - 1
    
    if linePos < 0 or linePos > 2:
        print("Sorry, this line does not exist.")
        return
    else: lineCorrect = True


#choose column
    print("And in which position shall we place your " + currentSymbol + " ?")
    columnChoice = input()
    if lineChoice.isdigit() == False:
       print("This is not a number.")
       return
    columnInt = int(columnChoice)
    columnPos = columnInt - 1

    if columnPos < 0 or columnPos > 2:
            print("Sorry, this position does not exist.")
            return
    else: columnCorrect = True

    possible()

def possible():
     global linePos
     global columnPos
     global emptySpace

     if gameboard[linePos][columnPos] == " ":
          emptySpace = True
     else:
          print("This move has already been made.")
          emptySpace = False
    
def winConditions():
    global win
    
    #lines
    for line in gameboard:
        if line == [currentSymbol, currentSymbol, currentSymbol]:
            win = True
    
    #columns
    if gameboard[0][columnPos] == gameboard[1][columnPos] == gameboard[2][columnPos]:
        win = True
    
    #diagonal
    if gameboard[0][0] and gameboard [1][1] and gameboard[2][2] == currentSymbol:
        win = True
    if gameboard[2][0] and gameboard [1][1] and gameboard[0][2] == currentSymbol:
            win = True

table()

while repeat:
    turn()
    
    if lineCorrect and columnCorrect and emptySpace == True:
        gameboard[linePos][columnPos] = currentSymbol
        winConditions()
        if win == True:
            repeat = False
            print("Well done, " + currentPlayer + ", you have won the game!")
        else: turnchanger()
    else: print("Please choose another position for your '" + currentSymbol + "'.")
    
    table()
    
    lineCorrect = False
    columnCorrect = False