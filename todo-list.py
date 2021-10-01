#init variables
running = True
file = None

# the main code
while running:
  try:
    # getting the user input
    userinp = input()
    # spliting into args
    userinparg = userinp.split()

    if userinparg[0] == "open":
      file = open(userinparg[1], "a+")
    if userinparg[0] == "add-task":
      pass
    elif userinparg[0] == "quit":
      running = False
    else:
      print("command not found")
  except IndexError: # error handling stuff
    print("please enter a command")
  except EOFError:
    print("\nplease enter a command")
  except KeyboardInterrupt:
    print("\nplease enter a command")
  except OSError:
    print("open a list file first to use that command")

try:
  file.close()
except OSError:
  pass