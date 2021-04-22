try:
    value = input("What is your age? ")
    salary = 10000
    cala = 10000 / int(value)
    print(value)
    print(cala)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot be divide by 0")

