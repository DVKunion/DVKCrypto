# -*-coding: UTF-8 -*-
# Author DVK

import hashlib

def esha1(str):
    m = hashlib.sha1()
    m.update(str.encode("utf-8"))
    ans = m.hexdigest()
    return ans
def dsha1(str):
    pass
def esha256(str):
    m = hashlib.sha256()
    m.update(str.encode("utf-8"))
    ans = m.hexdigest()
    return ans
def esha512(str):
    m = hashlib.sha512()
    m.update(str.encode("utf-8"))
    ans = m.hexdigest()
    return ans
def esha224(str):
    m = hashlib.sha224()
    m.update(str.encode("utf-8"))
    ans = m.hexdigest()
    return ans
def esha384(str):
    m = hashlib.sha384()
    m.update(str.encode("utf-8"))
    ans = m.hexdigest()
    return ans