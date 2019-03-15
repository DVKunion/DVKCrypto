# -*-coding: UTF-8 -*-
# Author DVK

def casa(str):
    for i in range(0,26):
        nstr=''
        for k in str:
            if ord(k)>64 and ord(k)<91:
                t = (ord(k) + i - 65)%26
                nstr = nstr + chr(t + 65)
            elif ord(k)>96 and ord(k)<123:
                t = (ord(k) + i - 97)%26
                nstr = nstr + chr(t + 97)
            elif k == " ":
                nstr = nstr + " "
            else:
                nstr = '[ERROR] Caesar only support a-z or A-Z'
                break
        print 'vi =',
        print i,
        print nstr
def rot13(str):
    nstr=''
    for k in str:
        if ord(k) > 64 and ord(k) < 91:
            nstr=nstr+chr((ord(k)-65+13)%26+65)
        elif ord(k) > 96 and ord(k) < 123:
            nstr = nstr + chr((ord(k) - 97 + 13) % 26 + 97)
        elif k == " ":
            nstr = nstr + " "
    return nstr