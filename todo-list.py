running = True
file = None

while running:
  userinp = input()
  userinparg = userinp.split()
  try:
    if userinparg[0] == "open":
      file = open(userinparg[1], "r+")
    elif userinparg[0] == "quit":
      running = False
    else:
      print("command not found")
  except IndexError:
    print("please enter a command")

try:
  file.close()
except OSError:
  pass