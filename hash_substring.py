def rabikrap(text, pattern):

    galv = 101  
    x = 256  
    p = len(pattern)
    t = len(text)
    c = 0 
    d = 0 
    e = 1

    for i in range(p - 1):
        e = (e * x) % galv

    for i in range(p):
        c = (x * c + ord(pattern[i])) % galv
        d = (x * d + ord(text[i])) % galv

    notikumi = [] 


    for i in range(t - p + 1):

        if c == d:
            match = True
            for j in range(p):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                notikumi.append(i)


        if i < t - p:
            d = (x * (d - ord(text[i]) * e) + ord(text[i + p])) % galv

        
            if d < 0:
                d = d + galv

    return notikumi

ievgalv = input()
if ievgalv == "I":
    pattern = input().rstrip()
    text = input().rstrip()
elif ievgalv == "F":
    with open("test_sample.txt") as file:
        pattern = file.readline().rstrip()
        text = file.readline().rstrip()


notikumi = rabikrap(text, pattern)
print(*notikumi)
