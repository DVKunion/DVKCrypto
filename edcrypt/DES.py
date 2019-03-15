#encoding = utf-8
#DES module
from crypto.library.cryptor import DES

class DEScrypto:
	#defualt key:'AAAAAAAA'
	#defualt iv :'BBBBBBBB'
	#defualt mod :'ECB'
	key  = 'AAAAAAAA'
	iv   = 'BBBBBBBB'
	text = ''
	mod  = 'DES.MODE_ECB'
	modsel = ['DES.MODE_ECB','DES.MODE_CBC','DES.MODE_CTR','DES.MODE_OFB','DES.MODE_CFB']
	def __init__(self, key='',iv='',mod=''):
		if len(key) > 0:
			self.key = key
		if len(iv) > 0:
			self.iv	= iv
		self.mod = modsel[mod] 
	def encrypto(self,text):
		try:
			if self.mod == 'DES.MODE_ECB':
				cipherx = DES.new(self.key,self.mod)
			else :
				cipherx = DES.new(self.key,self.mod,self.iv)
			extend = 8 - len(text) % 8
			extendstr = ""
			for i in range(extend):
				extendstr = extendstr+chr(extend)
			text = text + extendstr
			x = cipherx.encrypt(text)
			return x.encode('hex_codec').upper()
		except:
			return "error!"
	def decrypto(self,text):
		try:
			if self.mod == 'DES.MODE_ECB':
				cipherx = DES.new(self.key,self.mod)
			else :
				cipherx = DES.new(self.key,self.mod,self.iv)
			extendpass  = 8 - len(text)%8
			for i in range(extend):
				extendstr = extendstr+chr(extend)
			text = text + extendstr
			x = cipherx.decrypt(text)
			return x.encode('hex_codec').upper()
		except:
			return "error!"
