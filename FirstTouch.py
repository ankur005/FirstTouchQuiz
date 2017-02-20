def SantaDelivers(givenPath):
    # Set storing the houses already visited by Santa
    visitedHouses = set()
    # Coordinates of Santa's location
    x = 0
    y = 0
    visitedHouses.add((x,y))

    # Update Santa's location i.e. coordinates after each move (according to the direction provided by the elf)
    for direction in givenPath:
        if direction == ">":
            x+=1
        elif direction == "<":
            x-=1
        elif direction == "^":
            y+=1
        else:
            y-=1
        visitedHouses.add((x,y))

    print "Houses that received atleast one present : " + str(len(visitedHouses))

def SantaRoboDelivers(givenPath):
    # Boolean to decide if Santa moved or the robot
    santaMoves = True
    visitedHouses = set()
    # Initial Coordinates of Santa
    sx = 0
    sy = 0
    # Initial Coordinates of Robot
    rx = 0
    ry = 0

    # Add starting position of Santa and Robot to houses visited set
    visitedHouses.add((sx,sy))

    # Update Santa's or robot's location after each move
    for direction in givenPath:
        # Check of the current direction/move is for Santa or Robot
        if santaMoves == True:
            if direction == ">":
                sx+=1
            elif direction == "<":
                sx-=1
            elif direction == "^":
                sy+=1
            else:
                sy-=1
            visitedHouses.add((sx, sy))
            santaMoves = False
        else:
            if direction == ">":
                rx+=1
            elif direction == "<":
                rx-=1
            elif direction == "^":
                ry+=1
            else:
                ry-=1
            visitedHouses.add((rx, ry))
            santaMoves = True

    print "Houses that received atleast one present : " + str(len(visitedHouses))

choice = raw_input("Please select any one option \n 1. Only Santa delivers presents \n 2. Santa and the robot delivers presents \n")
path = raw_input("Enter input path : ")
if choice == "1":
    SantaDelivers(path)
elif choice == "2":
    SantaRoboDelivers(path)
else:
    print "Invalid Choice. Program will exit..."