import re

keyfile = "/home/jogubaba/Downloads/devold.txt"
testfile = "/home/jogubaba/Downloads/allcheck.txt"

keys = set(key.lower() for key in
    re.findall(r'[\w\.-]+', open(keyfile, "r").readline()))

with open(testfile) as f:
    for line in f:
        words = set(word.lower() for word in re.findall(r'[\w\.-]+', line))
        if keys & words:
            print(line, end='')