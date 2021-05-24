
#variables deciding your starting position
x = 4
y = 0



#opening text
print("You wake up in a dark hallway, it's cold and unfamiliar")

#asking whether the user would like to begin playing
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
    print("You look back to infront of you and start moving")
    print()
    # controls explanation
    controls = input("Type 'H' for help or any other character to continue")
    if controls == 'H' or controls == 'h':
        print("W to move up, A to move left, S to move back, D to move down and R for descriptions")

    print()
        #The if else statements used to define movement
    mainmovement = input("What will you do?")
    if mainmovement == 'W' or mainmovement == 'w':
        print("You moved up one step")
        y + 1
    if mainmovement == 'S' or mainmovement == 's':
        print("You moved down one step")
        y - 1
    if mainmovement == 'A' or mainmovement == 'a':
        print("You moved left one step")
        x - 1
    if mainmovement == 'D' or mainmovement == 'd':
        print("You moved right one step")
        x + 1
    if x == 5 and y == 0:
        print("Test")





