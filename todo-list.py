from os import system
from random import randrange

running = True
file = None

def format_task(task): # will format the task item in file in a neat way.
    result = "task: " + task.split("|")[0] + "id:  " + task.split("|")[1]
    return result

while running:
    # getting input from user and stuff
    try:
      usrinp = input()
      usrinpargs = usrinp.split()
      filesplit = None # initizialing the filetxt stuff to be global

      if file != None:
        filesplit = file.read().split(";")
    
      if usrinpargs[0] == "open" or usrinpargs[0] == "create":
        file = open(usrinpargs[1], "a+")
      elif usrinpargs[0] == "print":
        for i in filesplit:
          print(i)
      elif usrinpargs[0] == "add-task":
        file.write(usrinpargs[1] + ";")
      elif usrinpargs[0] == "clear": # gets really annoying when so much stuff on the screen
        try:
          system("clear") # unix
        except OSError:
          system("cls") # windows
      else:
        print("command not found")

    except EOFError: # error handling
        print("\nplease enter a command")
    except IndexError: # more error handling
        print("please enter a command or put in more args")
    except (OSError, TypeError, AttributeError): # if user hasn't opened a todo list file yet
        print("must first open a file to use that command")