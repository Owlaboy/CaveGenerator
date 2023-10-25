from display import display

if __name__ == "__main__":
    """This file calls the program's main file. It asks the user for the wanted inputs
    """
    running = True
    while running:
        print("Welcome to the cave generator")
        print("What kind of cave would you like to generate?")

        sizeX = input("How wide would you like your map to be? default 1000. ")
        if sizeX == "":
            sizeX = 1000

        sizeY = input("How tall would you like your map to be? default 500. ")
        if sizeY == "":
            sizeY = 500

        roomCount = input(
            "How many rooms would you like your cave to have? default 10. ")
        if roomCount == "":
            roomCount = 10

        showAnimation = input(
            "Would you like to see an animation of the triangulation process? (Y/N) default N "
        )
        if showAnimation == "Y":
            showAnimation = True
        elif showAnimation == "N":
            showAnimation = False
        else:
            showAnimation = False

        running = display(int(sizeX), int(sizeY), int(roomCount), showAnimation)
