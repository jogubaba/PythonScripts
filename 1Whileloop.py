print("Hello World")
print("Lets do a small program")
command = ""
started = False
#stopped = False
while True:
    command = input(">").lower()
    if command == 'help':
        print("type start - to start the car")
        print("type stop - to stop the car")
        print('type quit - to quit from here')
    elif command == 'start':
        if started:
            print("Car is already started!")
        else:
            started = True
            print('Car has been started..')
    elif command == 'stop':
        if not started:
            print('Car is already stopped!')
        else:
            started = False
            print('Car has been stopped..')
    elif command == 'quit':
        print('Quitting this Program')
        break
    else:
        print('Wrong input, I did not understand that, try help!')

#print('type start - to start a car')
#print('type stop - to stop a car')
#print('type quit - to quit the car')
#        elif command == 'start':
#        print("Car is started")
#        if command == 'stop':
#           print("Car is stopped")
#        else:


#   break

