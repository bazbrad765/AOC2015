import hashlib

found = False
string_input = "ckczppom"
num = 0


while not found:
    a = string_input +str(num)
    encoded = a.encode("utf-8")
    hashed = hashlib.md5(encoded)
    digest = hashed.hexdigest()
    ans = digest[0:6]
    if ans == "000000":
        
        print(a)
        found = True
    else:
        num += 1