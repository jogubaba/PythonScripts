file = open('/home/jogubaba/Downloads/My List', 'r')
f_contents = file.readlines()
sn = open('/home/jogubaba/Downloads/servervmname', 'r')
contents = sn.readlines()
for f_contents in contents:
    print(contents)
else:
    print("Not in List")




#another

keywords = input("Please Enter keywords path as c:/example/ \n :")
keys = open((keywords), "r").readlines()
keys = keys.split(',')  # separates key strings
with open("/home/jogubaba/Downloads/file2.txt") as f:
    for line in f:
        for key in keys:
            if key.strip() in line:
                print(line)




# another




