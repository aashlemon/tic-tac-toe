from os import system
import json

running = True
tasks = {
    
}
notify = 0

# if user is using a file
openedfile = False
file = None

while running:
    if len(tasks) != 0:
        print("\nNumber of task(s) left: " + str(len(tasks)))
    try:
        usrinp = input("\nEnter in a command: ")
        inpargs = usrinp.split()

        if inpargs[0] == "quit":
            running = False

            if openedfile == True:
                if input("Save file (y/n)?") == "y":
                    file.write(tasks)
                    file.close()
                elif input("Save file (y/n)?") == "n":
                    file.close()
                else:
                    running = True
                    print("Please try again")
        elif inpargs[0] == "clear":
            try:
                system("clear")
            except OSError:
                system("cls")
        elif inpargs[0] == "print":
            for key in tasks:
                print(f"\n{key}: {tasks[key]}")
            if len(tasks) == 0:
                print("\nDone for the day!")
        elif inpargs[0] == "add":
            if inpargs[1] in tasks:
                print("Task name is the same as another task name")
            else:
                tasks[inpargs[1]] = "".join(usrinp.split(maxsplit=2)[2])
        elif inpargs[0] == "finish":
            del tasks[inpargs[1]]
        elif inpargs[0] == "edit":
            if inpargs[1] in tasks:
                tasks[inpargs[1]] = inpargs[2]
            else:
                print("Task not found")
        elif inpargs[0] == "open":
            try:
                openedfile = True
                file = open(inpargs[1], "w+")
                try:
                    tasks = json.loads(file.read())
                except json.decoder.JSONDecodeError:
                    print("Failed to read file")
            except FileNotFoundError:
                openedfile = False
                print("File not found")
        else:
            print("command not found")
    except IndexError:
        print("please enter a command / please enter more arguments")
    except EOFError:
        print("\nplease enter a command")