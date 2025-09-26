import pyttsx3
import random

# pyttsx3 needs to be installed via pip install pyttsx3.
'''
1 for snake
-1 for water
0 for gun
'''



print("Welcome to the \"Snake🐍 Water💧 Gun🔫\" Game")
pyttsx3.speak("Welcome to the Snake Water Gun Game")



print("""Here are the rules!! \n
Snake🐍  drinks Water💧: Snake wins
Water💧 douses Gun🔫: Water wins
Gun🔫 kills Snake🐍 : Gun wins
If both players choose the same, it’s a draw""")
pyttsx3.speak("Here are the rules")

print("")

print("""here's how to choose:
for snake: type s
for water: type w
for gun: type g
""")

print("")

YouDict = {"s":1, "w":-1, "g":0}                                             #this converts the s,w,g to its corresponding number
ReverseDict = {1:"Snake🐍 ", -1:"Water 💧", 0:"Gun 🔫"}
ReverseDict1 = {1:"Snake ", -1:"Water ", 0:"Gun "}                           #this reverse dict converts the number to corresponding word to let the user know what they chose
Computer = random.choice([1,-1,0])

def play_game():

    while True:
        try:
            YouChoice = (input("enter your choice(s for Snake🐍, w for Water💧, g for Gun🔫): ")).lower()
            if YouChoice not in YouDict:
                raise ValueError("invalid value entered, please enter s,w or g") #once valid choice is entered,it exits if statement and runs next line
            You = YouDict[YouChoice]                                             #this is inside the while true and try function so that it ensures you only convert the choice after validating it
                                                                                #the corresponding number is stored in this variable
            break
        except ValueError as e:
            print(e)


    #by now we have 2 numbers(variables), computer and you
    print(f"You chose: {ReverseDict[You]} \nComputer Chose: {ReverseDict[Computer]}")

    pyttsx3.speak(f"you Chose{ReverseDict1[You]} and the computer chose {ReverseDict1[Computer]}")

    diff = Computer - You
    if diff == 0:
        print("It's a draw!")
        pyttsx3.speak("It's a draw")
    elif diff == -2 or diff == 1:
        print("You win!")
        pyttsx3.speak("You Win")
    else:
        print("You lose!")
        pyttsx3.speak("You Lose")

play_game()

print("")


while True:
    print("Want another try?? \nType Y or N")
    pyttsx3.speak("Want another try?")
    print("")
    while True:
        try:
            Decision = input("Enter your decision(Y for Yes, N for No): ").upper()
            if Decision not in ["Y", "N"]:
                raise ValueError ("invalid input, please enter Y or N")
            break
        except ValueError as e:
            print(e)
    DecisionDict = {"Y":3,"N":4}

    AnotherTry = DecisionDict[Decision]


    if (AnotherTry == 3):
        print("alright! Here you go")
        print("")
        play_game()
    elif (AnotherTry == 4):
        print("No Worries. Hope you had fun!")
        break




