file = open('/home/jogubaba/Downloads/file1.txt', 'r')
f_contents = file.readlines()
sn = open('/home/jogubaba/Downloads/file2.txt', 'r')
contents = sn.readlines()
lines = 0
for line in f_contents:
    check = str(line)
    print(check,end="")
    if check in contents:
        print("True")
    else:
        print("NOT")