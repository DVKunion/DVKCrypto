# -*-coding: UTF-8 -*-
# Author DVK

try:
    from edcode import *
    print '\033[1;32m[+] Moudle edcode loading success. \033[0m'
except:
    print '\033[1;31m[Error]: Moudle edcode loading faild! \033[0m'
try:
    from edhash import *
    print '\033[1;32m[+] Moudle edhash loading success. \033[0m'
except:
    print '\033[1;31m[Error]: Moudle edhash loading faild! \033[0m'


def HELP():
    print 'usage: main.py -h = get help  \n' \
          '               --eb64="xxx"    base64 encrypto  --db64="xxx" base64 decrypto \n' \
          '               --eb32="xxx"    base32 encrypto  --db32="xxx" base32 decrypto \n' \
          '               --eb16="xxx"    base16 encrypto  --db16="xxx" base16 decrypto \n' \
          '               --emd5="xxx"    md5    encrypto \n' \
          '               --esha1="xxx"   sha1   encrypto \n' \
          '               --esha224="xxx" sha224 encrypto \n' \
          '               --esha256="xxx" sha256 encrypto \n' \
          '               --esha384="xxx" sha384 encrypto \n' \
          '               --esha512="xxx" sha512 encrypto \n' \
          '               --casa="xxx"    caesar encrypto \n'\
          '               --rot13="xxx"   rot13  encrypto \n'

def do(slef,opt,arg):
    if opt == '-h':
        HELP()
    elif opt in ("--eb64"):
        print '\033[1;36m[ok] base64 encoding result:\033[0m'
        print base.eb64(arg)
    elif opt in ("--db64"):
        print '\033[1;36m[ok] base64 decoding result:\033[0m'
        print base.db64(arg)
    elif opt in ("--eb32"):
        print '\033[1;36m[ok] base32 encoding result:\033[0m'
        print base.eb32(arg)
    elif opt in ("--db32"):
        print '\033[1;36m[ok] base32 decoding result:\033[0m'
        print base.db32(arg)
    elif opt in ("--eb16"):
        print '\033[1;36m[ok] base16 encoding result:\033[0m'
        print base.eb16(arg)
    elif opt in ("--db16"):
        print '\033[1;36m[ok] base16 decoding result:\033[0m'
        print base.db16(arg)
    elif opt in ("--emd5"):
        ans=MD5.emd5(arg)
        print '\033[1;35m[ok] MD5(32) encoding result:\033[0m'
        print '[upper] ' + ans.upper()
        print '[lower] ' + ans
        print '\033[1;35m[ok] MD5(16) encoding result:\033[0m'
        print '[upper] ' + ans[8:24].upper()
        print '[lower] ' + ans[8:24]
    elif opt in ("--dmd5"):
        print 'rebuilding-----------'
        print 'please wait----------'
        #if opt in ("--path",'-p'):
        #    ans = MD5.dmd5(arg,p)
        #else:
        #    ans = MD5.dmd5(arg)
    elif opt in ("--esha1"):
        ans = SHA.esha1(arg)
        print '\033[1;35m[ok] sha1 encoding result:\033[0m'
        print ans
    elif opt in ("--dsha1"):
        print 'rebuilding-----------'
        print 'please wait----------'
    elif opt in ("--esha224"):
        ans = SHA.esha224(arg)
        print '\033[1;35m[ok] sha224 encoding result:\033[0m'
        print ans
    elif opt in ("--esha256"):
        ans = SHA.esha256(arg)
        print '\033[1;35m[ok] sha256 encoding result:\033[0m'
        print ans
    elif opt in ("--esha384"):
        ans = SHA.esha384(arg)
        print '\033[1;35m[ok] sha384 encoding result:\033[0m'
        print ans
    elif opt in ("--esha512"):
        ans = SHA.esha512(arg)
        print '\033[1;35m[ok] sha512 encoding result:\033[0m'
        print ans
    elif opt in ("--casa","-c"):
        print '\033[1;36m[ok] Caesar encoding result:\033[0m'
        caesar.casa(arg)
    elif opt in ("--rot13"):
        print '\033[1;36m[ok] Rot13 encoding result:\033[0m'
        print caesar.rot13(arg)