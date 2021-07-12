import string
import random
import re
s=string.ascii_lowercase
ss=list(s)
f=random.sample(s,26)
_in=open(input("input the plain text file: "),'r',encoding='utf-8')
out=open(input("output file name: "),'w')
plain=_in.read()
plain=plain.replace('\n','')

en_dict={}
for i in range(26):
    en_dict[ss[i]]=f[i]
cipher=""
for c in plain:
    if(c.lower() in en_dict):
        cipher+=en_dict[c.lower()]
    else:
        if(cipher[len(cipher)-1]!=' '):
            cipher+=" "
out.write(cipher)
out.close()
