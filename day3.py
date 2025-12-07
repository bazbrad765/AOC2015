visits = {""}
cur = 1


with open(r"C:\Users\bazbr\OneDrive\Desktop\Coding Projects\Python Projects\AOC\AOC2015\input3.txt","r") as f:
    f = f.read()

    for char in f:
        match char:
            case "^":
                cur += 1
                visits.add(cur)
            case "v":
                cur -= 1
                visits.add(cur)
            case ">":
                cur += 1000
                visits.add(cur)
            case "<":
                cur -= 1000
                visits.add(cur)

print(len(visits))

