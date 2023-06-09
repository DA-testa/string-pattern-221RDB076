def rabikraps(text, pattern):

    prime = 101  
    d = 256  
    pp = len(pattern)
    tt = len(text)
    p = 0 
    t = 0 
    h = 1
    for i in range(pp - 1):
        h = (h * d) % prime   
    for i in range(pp):
        p = (d * p + ord(pattern[i])) % prime
        t = (d * t + ord(text[i])) % prime

    notikumi = []
    for i in range(tt - pp + 1): 
        if p == t:
            match = True
            for j in range(pp):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                notikumi.append(i)
        if i < tt - pp:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + pp])) % prime
      
            if t < 0:
                t = t + prime
    return notikumi
text = None
pattern = None
    #\r\n\|??
"""
The prompt string, if given, is printed to standard output without a trailing newline before reading input.
NOT.
"""
input_choice = input().lstrip().rstrip()
if input_choice == "I":
    pattern = input().rstrip()
    if len(pattern)==0:
        pattern = input()
    text = input().rstrip()
elif input_choice == "F":
    with open("tests/06") as file:
        pattern = file.readline().rstrip()
        text = file.readline().rstrip()

notikumi = rabikraps(text, pattern)
print(*notikumi)
