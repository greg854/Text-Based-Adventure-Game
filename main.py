# variables deciding your starting position
X = 5
Y = 9

MAXIMUMX = 9
MAXIMUMY = 9


# A 10 x 10 floor layout
FLOOR_MAP = [['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W'],
             ['W', 'R3', 'R3', 'W', 'F', 'F', 'W', 'R4', 'R4', 'W'],
             ['W', 'R3', 'R3', 'D3', 'F', 'F', 'D4', 'R4', 'R4', 'W'],
             ['W', 'R3', 'R3', 'W', 'F', 'F', 'W', 'R4', 'R4', 'W'],
             ['W', 'W', 'W', 'W', 'W', 'F', 'W', 'W', 'W', 'W'],
             ['W', 'W', 'W', 'W', 'W', 'F', 'W', 'W', 'W', 'W'],
             ['W', 'R1', 'R1', 'R1', 'W', 'F', 'W', 'R2', 'R2', 'W'],
             ['W', 'R1', 'R1', 'R1', 'D1', 'F', 'D2', 'R2', 'R2', 'W'],
             ['W', 'R1', 'R1', 'R1', 'W', 'F', 'W', 'R2', 'R2', 'W'],
             ['W', 'W', 'W', 'W', 'W', 'F', 'W', 'W', 'W', 'W']]

# Room descirptions
ROOM_1 = "It seems to be a plain room. It has a large wooden desk in the middle with planks of it eroding. The rest of the room is covered in spiderwebs, dust and dead bugs. Odd, considering the clean wood designs in the hallway."
ROOM_2 = "It looks to be the kitchen. The fridge towards the back wall has no designs on it apart from the star rating. The rest of the kitchen seems to be empty with a few crumbs and some dust laying around"
ROOM_3 = "It's what seemed to be the living room. There's a big, mouldy couch in the middle. It has a chair next to it but nothing really stands out in this room."
ROOM_4 = "This room must have been the bedroom. Theres a small bed in the middle, just large enough for a fully grown adult with a bit of extra room."


def moveForward():
    global Y
    Y = Y + 1


def moveBack():
    global Y
    Y = Y - 1


def moveLeft():
    global X
    X = X - 1

def moveright():
    global X
    X = X + 1


def printLayout():
    for i in range(len(FLOOR_MAP)):
        print(FLOOR_MAP[i])

def printCurrentPosition():
    print("Row: {}, Column: {}").format(X, Y)

def ifIsInBounds(x,y):
    if x <= MAXIMUMX and x >= 0 and y >= 0 and y <= MAXIMUMY:
        return True
    return False

# Used to check if we are trying to move to a location where we hit a wall
# If this returns true, you can move to this location and update your current location
# otherwise, you can't and you shouldn't update your location
#return True if the player can move in that direction, otherwise return false
def isThisAWall(nextmove):
    if nextmove == 'W':
        futurepositionX = X
        futurepositionY = Y - 1
        futureposition = FLOOR_MAP[futurepositionY][futurepositionX]
        if (futureposition == 'W'):
            print("Can't move here, you hit a wall")
            return False

    elif nextmove == 'A':
        futurepositionX = X - 1
        futurepositionY = Y
        futureposition = FLOOR_MAP[futurepositionY][futurepositionX]
        if (futureposition == 'W'):
            print("Can't move here, you hit a wall")
            return False

    elif nextmove == 'S':
        futurepositionX = X
        futurepositionY = Y + 1
        futureposition = FLOOR_MAP[futurepositionY][futurepositionX]
        if (futureposition == 'W'):
            print("Can't move here, you hit a wall")
            return False

    elif nextmove == 'D':
        futurepositionX = X + 1
        futurepositionY = Y
        futureposition = FLOOR_MAP[futurepositionY][futurepositionX]
        if (futureposition == 'W'):
            print("Can't move here, you hit a wall")
            return False
    else:
        return True

def enteringRoomOne():
    if FLOOR_MAP[X][Y] == 'D1' or FLOOR_MAP[X][Y] == 'R1':
        #If we got here, we are at the doorway to room 1 or in the room
        return True
    return False

def enteringRoomTwo():
    if FLOOR_MAP[X][Y] == 'D2' or FLOOR_MAP[X][Y] == 'R2':
        # If we got here, we are at the doorway to room 2 or in the room
        return True
    return False

def enteringRoomThree():
    if FLOOR_MAP[X][Y] == 'D3' or FLOOR_MAP[X][Y] == 'R3':
        # If we got here, we are at the doorway to room 3 or in the room
        return True
    return False

def enteringRoomFour():
    if FLOOR_MAP[X][Y] == 'D4' or FLOOR_MAP[X][Y] == 'R4':
        # If we got here, we are at the doorway to room 4 or in the room
        return True
    return False



def play():
    global X
    global Y
    # opening text
    print("You wake up in a dark hallway, it's cold and unfamiliar")

    # asking whether the user would like to begin playing
    gameinitialise = input("Would you like to begin playing? Y for yes, N for no: ")
    if gameinitialise == 'N' or gameinitialise == 'n':
        print("You turn the other way and leave")
    elif gameinitialise == 'Y' or gameinitialise == 'y':
        print("You rub your eyes and look ahead of you")
        print()
        print("As your eyes begin to adjust to the dark hallway, you pull yourself to your feet")
        print()
        print("The house seems to be some sort of small 1 story place, with only about 4 rooms")
        print()
        print("Both the walls and the ground are made up of seemingly, newly replaced wooden planks")
        print()
        print("You look up and see an empty roof, maybe 2 meters tall or so")
        print()
        print("You look back to in front of you and start moving")
        print()
        # controls explanation
        controls = input("Type 'H' for help or any other character to continue ")
        if controls == 'H' or controls == 'h':
            print("W to move up\n A to move left\n S to move back\n D to move down\n R for descriptions\n E to exit the game\n Z to respawn")

        print()
        while True:

            # The if else statements used to define movement
            mainmovement = input("What will you do? ")
            if mainmovement == 'z' or mainmovement == 'Z':
                X = 5
                Y = 9
                print('Your vision blurs and you find yourself in the doorway again...')
                print()
                continue
            if mainmovement == 'e' or mainmovement == 'E':
                break
            if mainmovement == 'W' or mainmovement == 'w':
                if ifIsInBounds (X, Y - 1) == False:
                    print("You can't go further in this direction")
                    continue
                if isThisAWall('W') == False:
                    print("You moved up one step")
                    moveForward()
            elif mainmovement == 'S' or mainmovement == 's':
                if ifIsInBounds (X, Y + 1) == False:
                    print("You can't go further in this direction")
                    continue
                if isThisAWall('S') == False:
                    print("You moved down one step")
                    moveBack()
            elif mainmovement == 'A' or mainmovement == 'a':
                if ifIsInBounds (X - 1, Y) == False:
                    print("You can't go further in this direction")
                    continue
                if isThisAWall('A') == False:
                    print("You moved left one step")
                    moveLeft()
            elif mainmovement == 'D' or mainmovement == 'd':
                if ifIsInBounds (X + 1, Y) == False:
                    print("You can't go further in this direction")
                    continue
                if isThisAWall('D') == False:
                    print("You moved right one step")
                    moveright()
            elif mainmovement == 'R' or mainmovement == 'r':
                if enteringRoomOne() == True:
                    print(ROOM_1)
                elif enteringRoomTwo() == True:
                    print(ROOM_2)
                elif enteringRoomThree() == True:
                    print(ROOM_3)
                elif enteringRoomFour() == True:
                    print(ROOM_4)
                # Check if we are in the hallway
                elif (FLOOR_MAP[X, Y] == 'F'):
                    print('You\'re in the hallway')
                else:
                    print()



if __name__ == '__main__':
    # Which function to run first, if we are running this as a module
    # Remove the pound sign below this if you want to have a diagram of the map
    #printLayout()
    play()
