list = [7,7,2,1,2,8,5,12,4,7,2]
#dup = list[0]
#print(dup)
for every in list:
    if list.count(every) >= 2:
        list.remove(every)
print(list)

numbers = [2,2,4,3,5,6,9,1,9]
dupli = []
for ever in numbers:
    if ever not in dupli:
        dupli.append(ever)
print(dupli)




