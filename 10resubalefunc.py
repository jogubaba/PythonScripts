list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def tables(number):
    for every in list:
        return every * int(number)


output = input("Which table do you want to see? ")
table = tables(output)
print(table)