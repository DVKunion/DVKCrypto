import vigenerecipher
import io
Ciphertext ='rla xymijgpf ppsoto wq u nncwel ff tfqlgnxwzz sgnlwduzmy vcyg ib bhfbe u tnaxua ff satzmpibf vszqen eyvlatq cnzhk dk hfy mnciuzj ou s yygusfp bl dq e okcvpa hmsz vi wdimyfqqjqubzc hmpmbgxifbgi qs lciyaktb jf clntkspy drywuz wucfm'
f=open('D:\\Users\\Desktop\\crypty\\keys.txt','r')



for i in range(0,10000):
	Key=f.readline()
	kt=len(Key)
	Key=Key[0:kt-1]
	Ciphertext =Ciphertext.replace(' ','')
	Key=Key.replace(' ','')
	l=len(Ciphertext)
	k=len(Key)
	cnt=0
	for i in range(k,l):
		if i%k == 0:
			cnt=0
		else:
			cnt=cnt+1
		Key=Key+Key[cnt]
	ClearText = vigenerecipher.decode(Ciphertext,Key)
	print(ClearText)


