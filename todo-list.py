from os import system

running = True
tasks = {
    "task one": "test"
}
notify = 0

while running:
    if len(tasks) != 0:
        print("Number of task(s) left: " + str(len(tasks)))
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
        elif inpargs[0] == "print":
            for key in tasks:
                print("\ntask name: " + key + "\ntask: " + tasks[key] + "\n")
        else:
            print("command not found")
    except IndexError:
        print("please enter a command / please enter more arguments")
    except EOFError:
        print("\nplease enter a command")