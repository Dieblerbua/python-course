print("")
print("Good morning, players! Please assume fighting positions. ")
print("The following game was common among people of the 21st century and was named 'Tik Tak Toe'.")
print("The rules for this ancient game were discovered by the great archeologist Dr. Lillith Clawthorne.")
print("It is played upon a 3 by 3 grid, in which you will fill in the symbols X and O.")
print("The first player to get three in a row wins. Good luck!")

player1 = input("Player 1, please state your name: ")
player2 = input("Player 2, how may I call you? ")
gameboard = [[" "," "," "],[" "," "," "],[" "," "," "]]

for line in gameboard:
    for position in line:
        print(position, end = "")
    print("")

turnOf1 = True
row1correct = False
colum1correct = False
turnOf2 = False
row2correct = False
colum2correct = False
repeat = True
while repeat:
    
    #Turn of Player 1
    while turnOf1:
        print(player1 + ", which row would you like to place an X in?")
        row1 = input("")
        print("Alright " + player1 + ", and which column will you choose?")
        colum1 = input("")

        row1int = int(row1)
        colum1int = int(colum1)
        rowchoice1 = row1int - 1
        columchoice1 = colum1int - 1

        #check if possible
        if rowchoice1 < 0 or rowchoice1 > 2:
            print("Sorry, there is no such row in the game")
            row1correct = False
        else:
            row1correct = True

        if columchoice1 < 0 or columchoice1 > 2:
            print("Sorry, there is no such position in the game.")
            colum1correct = False
        else:
            colum1correct = True


        while row1correct and colum1correct:
            #check if empty
            if gameboard[rowchoice1][columchoice1] == " ":
                gameboard[rowchoice1][columchoice1] = "X"
                turnOf1 = False
            else:
                print("Sorry, this field is already occupied. Choose a different one!")
                turnOf1 = True

            #reprint gameboard
            print("")
            for line in gameboard:
                for position in line:
                    print(position, end = "")
                print("")
            turnOf2 = True

            #Win conditions
            for line in gameboard:
                if line == ["X", "X", "X"]:
                    repeat = False
                    turnOf2 = False
                    print("Well done, " + player1 + ". You have won the game!")
            row1correct = False
            colum1correct = False
            turnOf1 = False


    #turn of Player 2
    while turnOf2:
        print(player2 + ", which row would you like to place an O in?")
        row2 = input("")
        print("Alright " + player2 + ", and which column will you choose?")
        colum2 = input("")

        row2int = int(row2)
        colum2int = int(colum2)
        rowchoice2 = row2int - 1
        columchoice2 = colum2int - 1

         #check if possible
        if rowchoice2 < 0 or rowchoice2 > 2:
            print("Sorry, there is no such row in the game")
            row2correct = False
        else:
            row2correct = True

        if columchoice2 < 0 or columchoice2 > 2:
            print("Sorry, there is no such position in the game.")
            colum2correct = False
        else:
            colum2correct = True


        while row2correct and colum2correct:

            #check if empty
            if gameboard[rowchoice2][columchoice2] == " ":
                gameboard[rowchoice2][columchoice2] = "O"
                turnOf2 = False
            else:
                print("Sorry, this field is already occupied. Choose a different one!")
                turnOf2 = True

            #reprint gameboard
            print("")
            for line in gameboard:
                for position in line:
                    print(position, end = "")
                print("")
            turnOf1 = True

            #Win conditions
            for line in gameboard:
                if line == ["O", "O", "O"]:
                    repeat = False
                    turnOf1 = False
                    print("Well done, " + player2 + ". You have won the game!")
            row2correct = False
            colum2correct = False
            turnOf2 = False