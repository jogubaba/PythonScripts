file = open('/home/jogubaba/Downloads/file1.txt', 'r')
f_contents = file.readlines()
sn = input("Enter patj of second file", 'r')
for keys in f_contents:
      with open(sn) as f:
            for line in f:
                  words = set(word.lower() for word in re.findall(r'[\w\.-]+', line))
                  if keys & words:
                        print(line, end='')

