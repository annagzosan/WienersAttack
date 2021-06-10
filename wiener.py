# -*- coding: utf-8 -*-
"""
Created on Thu May 27 10:57:51 2021

@author: user
"""
import math
import base64



def fast(a, g, N):
    g_bin = bin(g)
    
    x = int(a,base=10)        #where a=the current letter xi
    d = 1
    for i in range(len(g_bin) -1, 1, -1):
        if (g_bin[i] == '1'):
            d = (d*x) % N
        x = (x**2) % N

    return d

def continuous_fraction(N,e):
    a=[-1 for i in range(0,1000)]
    a[0]=0
    i=1
    while N/e>0:
        temp=N
        N=e
        e=temp
        x=e/N
        a[i]=math.floor(x)
        e=e-(N*a[i])
        i=i+1
        if (e==0):
            break
    a_=[a[i] for i in range(0,i)]
    return a_
        


def k_d(a):

    kd=[[0 for x in range(0,2)] for y in range(0,len(a))]
    kd[1][0]=1
    kd[1][1]=a[1]
    for i in range(2,len(a)):
        ar=1
        par=1
        temp1=a[i]
        for j in range(i,1,-1):
            par=a[j-1]*temp1+ar
            ar=temp1
            temp1=par
        kd[i][0]=ar
        kd[i][1]=par
    return kd
            
def f_(e,k,d):
    return int((e*d - 1)/k)

def eq(N,f):
    temp=-N+f-1
    D=int(temp**2-4*N)
    if (D<0):
        return False
    if (D==0):
        if (temp==N):
            return True
    
    x1=int(temp-math.sqrt(D))
    x1=int(x1/2)
    x2=int(temp+math.sqrt(D))
    x2=int(x2/2)
   # print(x1,"   ",x2)
   # print(x1*x2)
    return x1*x2==N
        
def check_effectiveness(N,d):
    return N**(1/4)/3>d



N=194749497518847283
e=50736902528669041

#N=5697733
#e=3105251

a=continuous_fraction(N, e)

kd=k_d(a)
#print(kd)

d=0
for i in range(1,len(a)):
    f=f_(e,kd[i][0],kd[i][1])
    if(eq(N,f)):
        d=kd[i][1]
        print(d)
        break

if (check_effectiveness(N,d)):
    print("All good")
else:
    print("Not good bro")


d=20881
cipher_text="Qz1bNDc0MDYyNjMxOTI2OTM1MDksNTEwNjUxNzgyMDExNzIyMjMsMzAyNjA1NjUyMzUxMjg3MDQsODIzODU5NjMzMzQ0MDQyNjgNCjgxNjkxNTY2NjM5Mjc5MjksNDc0MDYyNjMxOTI2OTM1MDksMTc4Mjc1OTc3MzM2Njk2NDQyLDEzNDQzNDI5NTg5NDgwMzgwNg0KMTEyMTExNTcxODM1NTEyMzA3LDExOTM5MTE1MTc2MTA1MDg4MiwzMDI2MDU2NTIzNTEyODcwNCw4MjM4NTk2MzMzNDQwNDI2OA0KMTM0NDM0Mjk1ODk0ODAzODA2LDQ3NDA2MjYzMTkyNjkzNTA5LDQ1ODE1MzIwOTcyNTYwMjAyLDE3NDYzMjIyOTMxMjA0MTI0OA0KMzAyNjA1NjUyMzUxMjg3MDQsNDc0MDYyNjMxOTI2OTM1MDksMTE5MzkxMTUxNzYxMDUwODgyLDU3MjA4MDc3NzY2NTg1MzA2DQoxMzQ0MzQyOTU4OTQ4MDM4MDYsNDc0MDYyNjMxOTI2OTM1MDksMTE5MzkxMTUxNzYxMDUwODgyLDQ3NDA2MjYzMTkyNjkzNTA5DQoxMTIxMTE1NzE4MzU1MTIzMDcsNTI4ODI4NTEwMjYwNzI1MDcsMTE5MzkxMTUxNzYxMDUwODgyLDU3MjA4MDc3NzY2NTg1MzA2DQoxMTkzOTExNTE3NjEwNTA4ODIsMTEyMTExNTcxODM1NTEyMzA3LDgxNjkxNTY2NjM5Mjc5MjksMTM0NDM0Mjk1ODk0ODAzODA2DQo1NzIwODA3Nzc2NjU4NTMwNiw0NzQwNjI2MzE5MjY5MzUwOSwxODU1ODIxMDUyNzUwNTA5MzIsMTc0NjMyMjI5MzEyMDQxMjQ4DQoxMzQ0MzQyOTU4OTQ4MDM4MDYsODIzODU5NjMzMzQ0MDQyNjgsMTcyNTY1Mzg2MzkzNDQzNjI0LDEwNjM1NjUwMTg5MzU0NjQwMQ0KODE2OTE1NjY2MzkyNzkyOSw0NzQwNjI2MzE5MjY5MzUwOSwxMDM2MTA1OTcyMDYxMDgxNiwxMzQ0MzQyOTU4OTQ4MDM4MDYNCjExOTM5MTE1MTc2MTA1MDg4MiwxNzI1NjUzODYzOTM0NDM2MjQsNDc0MDYyNjMxOTI2OTM1MDksODE2OTE1NjY2MzkyNzkyOQ0KNTI4ODI4NTEwMjYwNzI1MDcsMTE5MzkxMTUxNzYxMDUwODgyLDgxNjkxNTY2NjM5Mjc5MjksNDc0MDYyNjMxOTI2OTM1MDkNCjQ1ODE1MzIwOTcyNTYwMjAyLDE3NDYzMjIyOTMxMjA0MTI0OCwzMDI2MDU2NTIzNTEyODcwNCw0NzQwNjI2MzE5MjY5MzUwOQ0KNTI4ODI4NTEwMjYwNzI1MDcsMTE5MzkxMTUxNzYxMDUwODgyLDExMTUyMzQwODIxMjQ4MTg3OSwxMzQ0MzQyOTU4OTQ4MDM4MDYNCjQ3NDA2MjYzMTkyNjkzNTA5LDExMjExMTU3MTgzNTUxMjMwNyw1Mjg4Mjg1MTAyNjA3MjUwNywxMTkzOTExNTE3NjEwNTA4ODINCjU3MjA4MDc3NzY2NTg1MzA2LDExOTM5MTE1MTc2MTA1MDg4MiwxMTIxMTE1NzE4MzU1MTIzMDcsODE2OTE1NjY2MzkyNzkyOQ0KMTM0NDM0Mjk1ODk0ODAzODA2LDU3MjA4MDc3NzY2NTg1MzA2XQ=="
cipher=base64.b64decode(cipher_text).decode('utf-8')
cipher = cipher.replace('\r\n', ',')
cipher = cipher.replace('C=[', '')
cipher = cipher.replace(']', '')
cipher = cipher.split(',')
print(cipher)
ascii_m=[fast(c, d, N) for c in cipher]
print(ascii_m)
text= [''.join(chr(i) for i in ascii_m)]
print(text)
