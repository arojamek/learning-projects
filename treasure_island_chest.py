print('''
*****************************************************************************
          |                   |                  |                     |
 ________|_______________.="";=.______________|_____________________|______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                "=._o"=._      `"=.                     |
 ________|____________________:=._o "=._.".-="'"=.__________________|______
|                   |    _.--" , ; `"=._o." ,-"""-. ".   |
|___________________|_._"  ,. .`  `` ,  "-._"-._   ". '_|__________________
          |           |o`"=._ , " `; .". ,  "-._"-._; ;              |
 ________|___________| ;`-.o`"=.; ."  '."\` . "-._ /_______________|_______
|                   | |o;    "-.o"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) -.o "=.`_.--"o.-; ;___|__________________
___/______/______/___|o;.    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
___/______/______/______/_"=._o--._   ;o|o;     .;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"/______/______/______/
___/______/______/______/______/____"=.o|o_.--""__/______/______/______/___
/______/______/______/______/______/______/______/______/______/______/_____ /
*****************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")



choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")