def weight_calculator():
    wght = int(input('Hello, What is your weight? '))
    ask = input("Is your weight in K's or P's? ")
    if ask.upper() == 'P':
        kilo = wght * 0.45
        return "Your weight in kilo is : " + str(kilo)
    elif ask.upper() == 'K':
        pound = wght / 0.45
        return "Your weight in pounds is : " + str(pound)
    else:
        return "Invalid option, I asked if in Pounds(L) or Kilo(K) only"


def get_name():
    print("Hi Dear")
    name = input("What is your name? ")
    return name


def calcu_add():
    print("Now, lets do some addition")
    x = int(input("Value for first number "))
    y = int(input("Value for second number "))
    add = x + y
    return add

