#!/usr/bin/python3
import sys
# variables are under this line

# an inventory, which is initially empty
inventory = []
move = ""
# start the player in the Hall
currentRoom = 'Lobby'
# random quiz round counter
roundCount = 0
# descriptions to each stuff
description = {
    'key': 'A mysterious key that might unlock a special passage...',
    'cookie': 'If you eat this cookie, you might regret it later...',
    'sword': 'Sharp blade, sharp mind...',
    'monster': 'An enemy has approached! Will you survive this encounter?',
    'potion': 'Will this help? Who knows...',
    'excalibur': 'So shiny......'
}

# a dictionary linking a room to other rooms
rooms = {

    'Lobby': {
        'south': 'Cave',
        'east': 'Castle',
        'item': ['sword']
    },
    'Dungeon': {
        'north': 'Hall',
        'item': 'monster',
    },
    'Cave': {
        'west': 'Lobby',
        'south': 'Garden',
        'item': ['potion'],
        'north': 'Castle',
    },
    'Garden': {
        'north': 'Cave',
        'item': ['key']
    },
    'Castle': {
        'south': 'Cave',
        'east': 'Augusta',
        'west': 'Sawgrass',
        'item': ['cookie']
    },
    'Bedroom': {
        'north': 'Dungeon',
        'west': 'Lobby',
        'item': ['excalibur']
    },
    "Augusta": {
        'north': 'Castle',
        'item': 'tiger'
    },
    'Sawgrass': {
        'south': 'Cave',
        'item': 'rory'
    }
}


def showInstructions():
    # print a main menu and the commands
    print('''
RPG Game
========
Commands:
  go [north, east, south, west]
  get [item]
  teleport [the places are secret.. you will find out more once you play the game] - beware of using this.. could land you in trouble
  quit [quit the game]
''')


# one time call to show instructions for the game
showInstructions()


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if "item" in rooms[currentRoom] and len(rooms[currentRoom]['item']) != 0:
        print('You see a ' + str(rooms[currentRoom]['item']))
    print("Type 'help' to get a full list of the commands again.")
    print("---------------------------")


# loop forever
while True and move != ["quit"]:
    showStatus()
    # get the player's next 'move'
    # .split() breaks it up into an list array
    # eg typing 'go east' would give the list:
    # ['go','east']
    move = ''
    while move == '':
        move = input('Enter command: ')

    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]
    move = move.lower().split(" ", 1)

    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # teleport to a special room
    if move[0] == "teleport":
        if move[1].capitalize() in rooms:
            currentRoom = move[1].capitalize()
        else:
            print("You can't teleport there!")

    # get command
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            print('Got the ' + move[1] + "!")
            print(description[move[1]])
            # delete the item from the room
            # del rooms[currentRoom]['item']
            rooms[currentRoom]['item'].remove(move[1])
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    if move[0] == 'help':
        print('''
Commands:
go [north, east, south, west]
get [item]
teleport [lobby, dungeon, cave, garden, or castle] - beware of using this.. could land you in trouble
quit [quit the game]
        ''')

    ## Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory and 'cookie' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... Since you did not eat the cookie, You win!!')
        break

    # Sword is not OP
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom][
        'item'] and "sword" in inventory and "cookie" not in inventory and "excalibur" not in inventory:
        print("Your sword was no match for the monster. You do no possess what is needed to survive. Game over!!")
        break

    # Excalibur sword is OP
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item'] and 'excalibur' in inventory:
        print("You possess an unbelievable amount of power. The monster was no match for your blade! You have won!!")
        break

    # Random golf quiz
    if 'item' in rooms[currentRoom] and 'tiger' in rooms[currentRoom]['item']:
        while True:
            roundCount += 1
            print("How many major championships has Tiger Woods won?")
            answer = input("The answer: ")
            if answer == "15":
                print("Correct! You will be sent back to the Lobby")
                # if you pass the quiz, it will delete it and never show up again.
                del rooms[currentRoom]['item']
                currentRoom = "Lobby"
                break
            # if you cannot pass the quiz the game will quit!
            elif roundCount == 3:
                print("You have lost your life. How could not know the answer to this question? Game over!!")
                sys.exit()
            else:
                print("Incorrect, you have a limited number of chances before you are faced with a judgement.")

    # Random golf quiz#2
    if 'item' in rooms[currentRoom] and 'rory' in rooms[currentRoom]['item']:
        while True:
            roundCount += 1
            print("How many major championships has Rory McIlroy won?")
            answer = input("The answer: ")
            if answer == "4":
                print("Correct! You will be sent back to the Lobby")
                # if you pass the quiz, it will delete it and never show up again.
                del rooms[currentRoom]['item']
                currentRoom = "Lobby"
                break
            # if you cannot pass the quiz the game will quit!
            elif roundCount == 3:
                print("You have been spared. Since Rory is not the GOAT, you will have one more chance to continue playing the game...")
                del rooms[currentRoom]['item']
                currentRoom = "Lobby"
                break
            else:
                print("Incorrect, you have a limited number of chances before you are faced with a judgement.")
    # If a player enters a room with a monster
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('You are not prepared to face this monster. He has slain you. Game over!!')
        break
