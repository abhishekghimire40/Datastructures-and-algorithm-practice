#replace every occurence of pi in string with 3.14

def replacePi(s,c,num):
    if len(s) == 0 or len(s)==1:
        return s
    if s[0] + s[1] == c:
        return num + replacePi(s[2:],c,num)
    else:
        return s[0] + replacePi(s[1:],c,num)

print(replacePi("abcdefg","pi","3.14"))