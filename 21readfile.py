with open('/home/jogubaba/Downloads/My List', 'r') as f:
    counter = 0
    f_contents = f.read()
    lines = f_contents.split("\n")
    for i in lines:
        if i:
            counter += 1
    #print(f_contents)
    print("There are " + str(counter) + " lines in your file")
sn = open('/home/jogubaba/Downloads/servervmname', 'r')
contents = sn.readlines()
condition = 0
while condition <= counter:
    if f_contents in contents:
        print(contents)
    else:
        print("Not in List")
    condition += 1

    #break
#    if f_contents in contents:
#    print(f_contents)
#else:
#    print("not in list")

#condition += 1
#print(condition)
#break




