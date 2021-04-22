print("Hi Dear")
name = input("What is your name? ")
weight = int(input('Hello ' + name + ',' + " What is your weight? "))
#if weight not number

ask = input("Is your weight in Kgs(K) or Pounds(L)? ")
if ask.upper() == 'L':
    kilo = weight * 0.45
    print("Your weight in kilo is : " + str(kilo))
elif ask.upper() == 'K':
    pound = weight / 0.45
    print("Your weight in pounds is : " + str(pound))
else:
    print("Invalid option, I asked if in Pounds(L) or Kilo(K) only")
