print("")
print("Good morning, players! Please assume fighting positions. ")
print("The following game was common among people of the 21st century and was named 'Tik Tak Toe'.")
print("The rules for this ancient game were discovered by the great archeologist Dr. Lillith Clawthorne.")
print("It is played upon a 3 by 3 grid, in which you will fill in the symbols X and O.")
print("The first player to get three in a row wins. Good luck!")

player1 = input("Player 1, please state your name: ")
player2 = input("Player 2, how may I call you? ")
gameboard = [[" "," "," "],[" "," "," "],[" "," "," "]]

def table():
    print("----------")
    for line in gameboard:
        print("|", end = "")
        for position in line:
            print(position, "|", end = "")
        print("")
        print("----------")
    print("")


turnOf1 = True
row1correct = False
column1correct = False
turnOf2 = False
row2correct = False
column2correct = False
repeat = True

table()
while repeat:
    
    #Turn of Player 1
    while turnOf1:
        print(player1 + ", which row would you like to place an X in?")
        row1 = input("")
        print("Alright " + player1 + ", and which column will you choose?")
        column1 = input("")

        row1int = int(row1)
        column1int = int(column1)
        rowchoice1 = row1int - 1
        columnchoice1 = column1int - 1

        #check if possible
        if rowchoice1 < 0 or rowchoice1 > 2:
            print("Sorry, there is no such row in the game")
            row1correct = False
        else:
            row1correct = True

        if columnchoice1 < 0 or columnchoice1 > 2:
            print("Sorry, there is no such position in the game.")
            column1correct = False
        else:
            column1correct = True


        while row1correct and column1correct:
            #check if empty
            if gameboard[rowchoice1][columnchoice1] == " ":
                gameboard[rowchoice1][columnchoice1] = "X"
                turnOf1 = False
            else:
                print("Sorry, this field is already occupied. Choose a different one!")
                turnOf1 = True

            table()

            #Win conditions
            for line in gameboard:
                if line == ["X", "X", "X"]:
                    turnOf2 = False
                    repeat = False
                    print("Well done, " + player1 + ". You have won the game!")
                    break
                else:
                    turnOf2 = True
            row1correct = False
            column1correct = False
            turnOf1 = False

    #turn of Player 2
    while turnOf2:
        print(player2 + ", which row would you like to place an O in?")
        row2 = input("")
        print("Alright " + player2 + ", and which column will you choose?")
        column2 = input("")

        row2int = int(row2)
        column2int = int(column2)
        rowchoice2 = row2int - 1
        columnchoice2 = column2int - 1

         #check if possible
        if rowchoice2 < 0 or rowchoice2 > 2:
            print("Sorry, there is no such row in the game")
            row2correct = False
        else:
            row2correct = True

        if columnchoice2 < 0 or columnchoice2 > 2:
            print("Sorry, there is no such position in the game.")
            column2correct = False
        else:
            column2correct = True


        while row2correct and column2correct:

            #check if empty
            if gameboard[rowchoice2][columnchoice2] == " ":
                gameboard[rowchoice2][columnchoice2] = "O"
                turnOf2 = False
            else:
                print("Sorry, this field is already occupied. Choose a different one!")
                turnOf2 = True

            table()

            #Win conditions
            for line in gameboard:
                if line == ["O", "O", "O"]:
                    repeat = False
                    turnOf1 = False
                    print("Well done, " + player2 + ". You have won the game!")
                else:
                    turnOf1 = True
            row2correct = False
            column2correct = False
            turnOf2 = False