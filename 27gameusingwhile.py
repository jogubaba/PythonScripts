secret = 7
guess_count = 0
guess_limit = 3
print("Hi There!")
print("Let's play a Secret Number Game")
game = input("Are you interested in playing a small game, type Y or N? ")
if game.upper() == 'Y':
    print("Ok, great choice, Let's begin")
    print("Try and guess my secret number under 10, in 3 attempts? ")
    while guess_count < guess_limit:
        number = int(input("Your guesses are ? "))
        guess_count += 1
        if number == secret:
            print("Son of a Gun, you guessed it right!")
            print("Good Luck for your next attempt")
            break
    else:
        print("You Failed Dude! Better Luck Next Time")
        print("That is all for today, Good Bye and Have a Nice Day!")
elif game.upper() == 'N':
    print("You are of no use, Go play your kido games like Ludo")