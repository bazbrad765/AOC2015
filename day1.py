floor = 0

with open(r"input1.txt","r") as f:
    text = f.read()
    for char in text:
        if char == "(":
            floor += 1
        else:
            floor -= 1
            
        print("New Floor: ",floor)

print(floor)