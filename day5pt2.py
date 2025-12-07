vowels = ["a","e","i","o","u"]
bad_strings = ["ab","cd","pq","xy"]
nice_strings = 0

with open("input5.txt","r") as f:
    
    for line in f:
        vowel_count = 0
        contains_double_up = False
        no_bad_strings = True
        for string in bad_strings:
            if string in line:
                no_bad_strings = False
                break

        for char in line:
            if char in vowels:
                vowel_count += 1


        for i in range(len(line) - 1):
            if line[i] == line[i + 1]:
                contains_double_up = True
        if contains_double_up and no_bad_strings and vowel_count >= 3:
            nice_strings += 1

print(nice_strings)

