nice_strings = 0

##FAILED

with open("input5.txt","r") as f:
    for line in f:
        print("Target Line: ", line)
        contains_double_up = False
        w = False
        

        for i in range(len(line) - 2):
            if line[i] == line[i + 2]:
                contains_double_up = True


        count = 0
        for i in range(len(line)):
        
            target = line[i:(i+2)]

            print("target:  ", target)
            if len(target) >=2:
                
                if target in line:
                    count += 1
                    print("Hit found, current hits: ", count, "on target ", target)
                    if count >= 2:
                        w = True
                        count = 0
                        print("2 found - breaking  from function")

 
        if contains_double_up and w:
            nice_strings += 1
        
print(nice_strings)




 