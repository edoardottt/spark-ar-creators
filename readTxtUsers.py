with open("data.txt", "r") as f:
    text = f.read().split(",")

users = []

for elem in list(set(text)):
    users.append(
        elem.replace('"', "").replace("\\", "").replace("[", "").replace("]", "")
    )

with open("usersTxt.txt", "w+") as f:
    for elem in users:
        f.write(elem + "\n")
