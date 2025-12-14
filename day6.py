import numpy as np
import re


lights_array = np.zeros((1000,1000), dtype=bool)

def process_lights(t: str):

    start_digits = re.findall(r"\d+(?=,)",t)
    start_digits = int(start_digits[0])
    end_digits = re.findall(r"\d+",t)
    end_digits = int(end_digits[1])
  
    start_digits2 = re.findall(r"\d+(?=,)",t)
    start_digits2 = int(start_digits2[1])
    end_digits2 = re.findall(r"\d+",t)
    end_digits2 = int(end_digits2[3])

    print(start_digits,end_digits)
    print(start_digits2,end_digits2)

    if t[1] == "u":
        if t[6] == "n":
            for light in lights_array[start_digits:end_digits,start_digits2:end_digits2]:
                light = True
                print("turned light on")
        else:

            for light in lights_array[start_digits:end_digits,start_digits2:end_digits2]:
                light = False
                print("turned light off")
    else:
        for light in lights_array[start_digits:end_digits,start_digits2:end_digits2]:
            if light == True:
                light = False
            else:
                light = True

count = 0
with open("input6.txt", "r") as f:
    for line in f:
        print(line)
        process_lights(line)
print(count)


                

