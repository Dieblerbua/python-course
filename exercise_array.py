#print array as a sentence

proto = ["My", "name", "is", "Elias"]

for x in proto:
    print(x, end = " ")
print("")

# Print only the word "is"

x = proto[2]
print(x)
print("")

# Print the 2-dimensional array

array0 = [["My", "name", "is", "Elias"], ["I", "am", "still", "alive"]]

for sentence in array0:
    for y in sentence:
        print(y, end = " ")    
    print("")

# Print only the words "name" and "am"

namista = array0[0][1]
think = array0[1][1]
print(namista)
print(think)

# Change the word "Elias" to "Su-zen"

array0[0][3] = "Su-Zen"
print(array0)

# Change the word "Elias" to a name determined by the user (tip: use input)

nameask = input("Or how may we adress you?")
print("Greetings, " + nameask)
array0[0][3] = nameask
print(array0)

# Print the sentences and let the user choose which word it wants to change and then change it. 

messingbusiness = [["My", "name", "is", "Elias"], ["I", "am", "still", "alive"]]

print("Good evening sire. It is about time we messed with the humans again.")
print("")
print("They have tried to state their name and prove their existence")
print("")
print("We cannot allow such tomfoolery, I shall leave the 'messing-up-business' to you")
print("")
print("If you would like to change anything in the first sentence, please type '0', or for the second sentence, type '1'")
sentencenumber = input("")
print("Now, which position should be changed, keep in mind that the first word starts at number '0'")
wordnumber = input("")
print("And which word would you like to replace this with?")
newword = input("")
print("As you wish, sire. Here is the result:")
print("")
print("")

sentencenumber = int(sentencenumber)
wordnumber = int(wordnumber)
messingbusiness[sentencenumber][wordnumber] = newword


for result in messingbusiness:
    for y in result:
        print(y, end = " ")    
    print("")

if(newword == "fart"):
    print("Very, funny, sir!")
else:
     print("You have done some wonderfull messing again, have a good night now, sir!")