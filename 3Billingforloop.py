Quantity = input("How many item's have you taken? ")
item = 0
list = 0
total = 0
while item < int(Quantity):
    Price = input("Enter price for the retail items you have taken one after the other ")
    for list in Price:
        total += int(list)
        print(list)
    print(total)
    item += 1
    break
