from os import system

running = True
tasks = {

}

while running:
    try:
        usrinp = input("Enter in a command: ")
        inpargs = usrinp.split()

        if inpargs[0] == "quit":
            running = False
        elif inpargs[0] == "clear":
            system("clear")
        else:
            print("command not found")
    except IndexError:
        print("please enter a command")
    except EOFError:
        print("please enter a command")