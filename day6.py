import numpy as np
import re

##FAILED!

lights_array = np.zeros((1000,1000), dtype=bool)
count = 0
def process_lights(t: str):

    start_digits = re.findall(r"\d+(?=,)",t)
    start_digits = int(start_digits[0])
    end_digits = re.findall(r"\d+",t)
    end_digits = int(end_digits[1])
  
    start_digits2 = re.findall(r"\d+(?=,)",t)
    start_digits2 = int(start_digits2[1])
    end_digits2 = re.findall(r"\d+",t)
    end_digits2 = int(end_digits2[3])

    print("Start Numbers: " +str(start_digits),str(end_digits))
    print("End Numbers: " +str(start_digits2),str(end_digits2))

    if t[1] == "u":
        if t[6] == "n":
            for light in lights_array[start_digits:end_digits],[start_digits2:end_digits2]:
                light = True
                print(light)
                #print("turned light on SB")
        else:

            for light in lights_array[start_digits:end_digits,start_digits2:end_digits2]:
                light = False
                #print("turned light off")
    else:
        for light in lights_array[start_digits:end_digits,start_digits2:end_digits2]:
            if light == True:
                light = False
            else:
                light = True



with open("input6.txt", "r") as f:
    for line in f:
        print(line)
        process_lights(line)
print(count)


                

