total = 0

with open(r"C:\Users\bazbr\OneDrive\Desktop\Coding Projects\Python Projects\AOC\AOC2015\input2.txt","r") as f:
    for line in f:
        new = line.split("x")
        new = [int(new[0]),int(new[1]),int(new[2])]
        print(new)
        ans = (2* (new[0]*new[1])) + (2* (new[1]*new[2])) + (2* (new[2]*new[0]))
        print("Required SQFootage:  " + str(ans))
        new.sort()
        smallest = new[0]*new[1]
        total += (ans + smallest)
print(total)


