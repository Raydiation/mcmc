import string
import math
import random
import re
import time
import os

def create_dec_dict(dec_key):
    dec_dict={}
    alpha_list=list(string.ascii_lowercase)
    for i in range(len(dec_key)):
        dec_dict[alpha_list[i]]=dec_key[i]
    return dec_dict

#decreption
def decrypt(text,dec_key):
    dec_dict=create_dec_dict(dec_key)
    text=list(text)
    plain=""
    for c in text:
        if(c.lower() in dec_dict):
            plain+=dec_dict[c.lower()]
        else:
            plain+=" "
    return plain
#

#Count reference score table
def score_ref(Ref_path):
    score_M2={}
    alpha_list=list(string.ascii_lowercase)
    with open(Ref_path,encoding="utf-8") as fp:
        for line in fp:
            ref=list(line.strip())
            for i in range(len(ref)-1):
                cha=ref[i].lower()
                chb=ref[i+1].lower()
                if(cha not in alpha_list and cha!=" "):
                    cha=" "
                if(chb not in alpha_list and chb!=" "):
                    chb=" "
                key=cha+chb
                if(key in score_M2):
                    score_M2[key]+=1
                else:
                    score_M2[key]=1
    return score_M2
#

#scoring a decreption key
def count_cipher(ciphertext):
    count_cip={}
    alpha_list=list(string.ascii_lowercase)
    cipher=list(ciphertext.strip())
    for i in range(len(cipher)-1):
        cha=cipher[i]
        chb=cipher[i+1]
        if(cha not in alpha_list and cha!=" "):
            cha=" "
        if(chb not in alpha_list and chb!=" "):
            chb=" "
        key=cha+chb
        if(key in count_cip):
            count_cip[key]+=1
        else:
            count_cip[key]=1
    return count_cip
def dec_scoring(ciphertext,dec_key,score_M2):
    decrypted_text=(decrypt(ciphertext,dec_key))
    dec_dict=count_cipher(decrypted_text)
    dec_score=0
    for key,val in dec_dict.items():
        if(key in score_M2):
            dec_score+=val*math.log(score_M2[key])
    return dec_score
#

#Generate cipher key
def rd_swap(dec_key):
    rand1=random.randint(0,25)
    while(1):
        rand2=random.randint(0,25)
        if(rand2!=rand1):
            break
    dec_Key=list(dec_key)
    tmp=dec_Key[rand1]
    dec_Key[rand1]=dec_Key[rand2]
    dec_Key[rand2]=tmp
    return "".join(dec_Key)
#

#Random(0,1) to accept new state
def rand_acc(p):
    uni=random.uniform(0,1)
    if(uni<p):
        return True
    return False    
#
#Main algorithm MCMC
def MCMC(Max_round,ciphertext,score_M2,start_key):
    cur_key=start_key
    cur_score=dec_scoring(ciphertext,cur_key,score_M2)
    best_key=""
    best_score=cur_score
    cnt=0
    keeping_cnt=0
    while(cnt<=Max_round):
        nxt_key=rd_swap(cur_key)
        nxt_score=dec_scoring(ciphertext,nxt_key,score_M2)
        acc_p=min(1,math.exp(nxt_score-cur_score))
        if(rand_acc(acc_p)):
            cur_key=nxt_key
            cur_score=nxt_score
        if(nxt_score>best_score):
            best_key=nxt_key
            best_score=nxt_score
            keeping_cnt=0
        else:
            keeping_cnt+=1
            if(keeping_cnt>10000):
                break;
        if(cnt%1000==0):
            print(cnt," rounds:\n",decrypt(ciphertext,cur_key),"\n\n")
        cnt+=1
    return best_key

#Input

Ref_path=(input("Reference text file name:"))
file=open(input("Ciphertext: "),'r',encoding='utf-8')
all_Cipher=file.read()
split_num=int(input("How long you would like to split your cipher if it's too long (>500 better):"))
Max_round=int(input("How many round of a mcmc algorithm :"))

#Prepare
score_M2=score_ref(Ref_path)
all_Cipher=all_Cipher.lower()
copy_Cipher=all_Cipher


#GO
part=0
dec_key=string.ascii_lowercase
while(1):
    if(len(all_Cipher)>split_num):
        pos=split_num
        while(all_Cipher[pos]!=' '):
            pos=pos-1
        pos+=1
        Cipher=all_Cipher[0:pos]
        all_Cipher=all_Cipher[pos:]
        dec_key=MCMC(Max_round,Cipher,score_M2,dec_key)
        part+=1
    else:
        Cipher=all_Cipher
        all_Cipher=""
        if(part==0):
            dec_key=MCMC(Max_round,Cipher,score_M2,dec_key)
    if(len(all_Cipher)==0):
        break
plain=decrypt(copy_Cipher,dec_key)
print("The plaintext we solved is :\n",plain)
file.close()
os.system("pause")
