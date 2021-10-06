from os import system

running = True
tasks = {

}
notify = 0

while running:
    if notify == 3:
            if len(tasks) != 0:
                print("Number of task left: " + len(tasks))

    if len(tasks) == 0:
        print("Done for the day!")

    try:
        usrinp = input("Enter in a command: ")
        inpargs = usrinp.split()

        if inpargs[0] == "quit":
            running = False
        elif inpargs[0] == "clear":
            try:
                system("clear")
            except OSError:
                system("cls")
        else:
            print("command not found")
    except IndexError:
        print("please enter a command")
    except EOFError:
        print("please enter a command")