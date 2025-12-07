floor = 0
char_num = 0

with open(r"C:\Users\bazbr\OneDrive\Desktop\Coding Projects\Python Projects\AOC\AOC2015\input1.txt","r") as f:
    text = f.read()
    for char in text:
        if char == "(":
            floor += 1
        else:
            floor -= 1
        char_num += 1
        if floor == -1:
            print(char_num)
        #print("New Floor: ",floor)

#print(floor)