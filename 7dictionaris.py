numbers = {
    "0" : "Zero",
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "10" : "Ten"
}
Phone = input("What is your phone number? ")
bus = ""
for every in Phone:
    word = (numbers.get(every)) + " "
    bus += word
print(bus)