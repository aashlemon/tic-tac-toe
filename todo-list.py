running = True
file = None

while running:
    try:
        pass
    except EOFError:
        print("\nplease enter a command")
    except IndexError:
        print("please enter a command")
    except OSError:
        print("please enter a command")