f = open("orders.txt", "w")
f.write("Pizza\nBurger\nSandwich\nPasta\nDosa\n")
f.close()

f = open("orders.txt", "r")

while True:
    line = f.readline()

    if not line:
        break

    print(line.strip())
    print("Position:", f.tell())

f.close()