santa_visits = {""}
robo_visits = {""}
combined = {}
s_cur = 0
r_cur = 0
santa_active = True


with open(r"C:\Users\bazbr\OneDrive\Desktop\Coding Projects\Python Projects\AOC\AOC2015\input3.txt","r") as f:
    f = f.read()
    for char in f:
        match char:


            case "^":
                if santa_active:
                    s_cur += 1
                    santa_active = False
                    santa_visits.add(s_cur)
                    
                else:
                    r_cur += 1
                    santa_active = True
                    robo_visits.add(r_cur)



            case "v":
                if santa_active:
                    s_cur -= 1
                    santa_active = False
                    santa_visits.add(s_cur)
                else:
                    r_cur -= 1
                    santa_active = True
                    robo_visits.add(r_cur)


            case ">":
                if santa_active:
                    s_cur += 1000000
                    santa_active = False
                    santa_visits.add(s_cur)
                else:
                    r_cur += 1000000
                    santa_active = True
                    robo_visits.add(r_cur)


            case "<":
                if santa_active:
                    s_cur -= 1000000
                    santa_active = False
                    santa_visits.add(s_cur)
                else:
                    r_cur -= 1000000
                    santa_active = True
                    robo_visits.add(r_cur)


combined = santa_visits.union(robo_visits)

print(len(combined) - 1)

