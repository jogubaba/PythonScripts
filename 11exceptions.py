try:
    age = int(input("What is your age? "))
    print(age)
except ValueError:
    print("Invalid Input")