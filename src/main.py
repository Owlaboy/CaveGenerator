from display import display

if __name__ == "__main__":
    """This file calls the program's main file. It asks the user for the wanted inputs
    """
    running = True
    setUp = True
    while running:
        if setUp:
            print("Welcome to the cave generator")
            print("What kind of cave would you like to generate?")

            sizeX = input("How wide would you like your map to be? (default 1000, min 300) ")
            if sizeX == "":
                sizeX = 1000

            sizeY = input("How tall would you like your map to be? (default 500, min 300) ")
            if sizeY == "":
                sizeY = 500

            roomCount = input(
                "How many rooms would you like your cave to have? (default 10, min 3) ")
            if roomCount == "":
                roomCount = 10

            showAnimation = input(
                "Would you like to see an animation of the triangulation process? (Y/N, default N) "
            )
            if showAnimation == "Y":
                speed = input("How fast should the animation be? Give a number between 100 and 2000. 100 being the fastest and 2000 the slowest. (default 1000) ")
                if speed == "":
                    speed = 1000
            else:
                speed = "0"

            print("To restart the program with the same inputs press spacebar. To close the program cloes the window or press the esc key. To restart the program press any other key.")

            if showAnimation == "Y":
                showAnimation = True
            elif showAnimation == "N":
                showAnimation = False
            else:
                showAnimation = False

        status = display(max((300,int(sizeX))), max((300,int(sizeY))),max((3, int(roomCount))), showAnimation, int(speed))
        running = status[0]
        setUp = status[1]

