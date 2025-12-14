import numpy as np
import re

#FAILED

lights_array = np.zeros((1000,1000), dtype=bool)
line_num = 1

def process_lights(t: str):
    global line_num
    start_digits = re.findall(r"\d+(?=,)",t)
    start_digits = int(start_digits[0])
    end_digits = re.findall(r"\d+",t)
    end_digits = int(end_digits[1])
  
    start_digits2 = re.findall(r"\d+(?=,)",t)
    start_digits2 = int(start_digits2[1])
    end_digits2 = re.findall(r"\d+",t)
    end_digits2 = int(end_digits2[3])


    print("Line # " , str(line_num))
    print("Instructions: " ,t)
    if t[1] == "u":
        if t[6] == "n": #turn on
            print("New Lights being tunrned ON")
            
            print("Start Numbers: " +str(start_digits),str(end_digits))

            print("End Numbers: " +str(start_digits2),str(end_digits2))
            

            lights_array[start_digits:end_digits,start_digits2:end_digits2] = True


        else:
            print("New Lights being tunrned OFF")
            print("Start Numbers: " +str(start_digits),str(end_digits))

            print("End Numbers: " +str(start_digits2),str(end_digits2))
            
            lights_array[start_digits:end_digits,start_digits2:end_digits2] = False

    else:
        print("New Lights being TOGGLED")
        print("Start Numbers: " +str(start_digits),str(end_digits))

        print("End Numbers: " +str(start_digits2),str(end_digits2))
        
        lights_array[start_digits:end_digits,start_digits2:end_digits2] = False if True else True

    print("\n")
    line_num += 1


with open("input6.txt", "r") as f:
    for line in f:
        process_lights(line)

count = 0
for i in lights_array:
    for a in i:
        if a == True:
            count += 1

print(count)


                

