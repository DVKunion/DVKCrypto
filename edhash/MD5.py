# -*-coding: UTF-8 -*-
# Author DVK

import hashlib

def emd5(str):
    m = hashlib.md5()
    m.update(str.encode("utf-8"))
    ans=m.hexdigest()
    return ans

def dmd5(str,mod,dic = None):
    if dic == None:
        print '\033[1;35m[ok] starting brute MD5 force:\033[0m'
    else:
        print '\033[1;35m[ok] starting check MD5 in dict:\033[0m'

