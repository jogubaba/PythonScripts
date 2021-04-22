cost = input("Whats up? ")
kill = cost.split(" ")
Emoticons = {
    "!" : "🤷‍🤷🤷#‍‍",
    "?" : "$"
}
bus = ""
for every in kill:
    line = Emoticons.get(every, every) + " "
    bus += line
print(bus)
