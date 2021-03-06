print("Hello")
print("Welcome to my pindi Girni Shop")
item = input("What is your item for Pindi Rubbudu today? ")
print("Ok, we will rubbify your item " + item + " now")
kg = input('How may KG is it of? ')
print("Sure, lets get your item started!")
print("Pour the " + item + " in the slot and you start the process on your own")
print("Use help if you need more info on the process")
#order = ""
started = False
while True:
    order = input("> ").lower()
    if order == 'start':
        if started:
            print("Machine is ON and your Rubbudu has started already")
        else:
            started = True
            print("You have started the rubbuding of your " + item + ' which is ' + str(kg) + "kgs")
    elif order == 'stop':
        if not started:
            print("Machine is already stopped")
        else:
            started = False
            print("The Rubbudu of " + item + " has stopped")
    elif order == 'quit':
        print("You have quitted the rubbudu process and the engine has stopped")
        break
    elif order == 'help':
        print("start - to start the rubbudu")
        print("stop - to stop the rubbudu")
        print("quit - to quit and stop the machine")
    else:
        print("Option Invalid, use Help option or type Quit to end the Process")



