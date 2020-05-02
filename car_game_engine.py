command = ""
state = ""
while command.lower() != "quit":
    command = input("> ")
    if command.lower() == "help":
        print("start - to start the car\nstop - to stop the car\nquit - to exit")
    elif command.lower() == "start":
        state.lower() = "start"
        print("Car started, ready to go!")
    elif command.lower() == "stop":
        state.lower() = "stop"
        print("Car stopped")
    elif command.lower() == "quit":
        break
    elif command.lower() == "start" and state == "start":
        print("Car already started")
    elif command.lower() == "stop" and state == "stop":
        print("Car already stopped")
    else:
        print("I do not understand the command")
else:
    print("Quit")
    
#or

command = ""
started = False
while command.lower() != "quit":
    command = input("> ")
    if command.lower() == "help":
        print("start - to start the car\nstop - to stop the car\nquit - to exit")
    elif command.lower() == "start":
        started = True
        print("Car started, ready to go!")
    elif command.lower() == "stop":
        started = False
        print("Car stopped")
    elif command.lower() == "quit":
        break
    elif command.lower() == "start" and started:
        print("Car already started")
    elif command.lower() == "stop" and not(started):
        print("Car already stopped")
    else:
        print("I do not understand the command")
else:
    print("Quit")
    