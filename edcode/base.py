# -*-coding: UTF-8 -*-
# Author DVK

import base64

def eb64(str):
    return base64.b64encode(str)
def db64(str):
    return base64.b64decode(str)
def eb32(str):
    return base64.b32encode(str)
def de32(str):
    return base64.b32decode(str)
def eb16(str):
    return base64.b16encode(str)
def db16(str):
    return base64.b16decode(str)