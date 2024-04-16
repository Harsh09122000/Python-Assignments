#Question-1

'''def num(a):
    if a%2==0:
        print('True')
    else:
        print("False")

a=int(input("enter the number:"))
num(a)'''

#Question-2

'''def fun(l):
    for i in l:
        if i%11==0:
            print(i,end=" ")


a=list(map(int,input('enter the numbers:').split()))
fun(a)'''

#Question-3
#Method-1

'''def fun_pal(c):

    for i in range(len(c)):
        if a[i]==a[-i-1]:
            continue
        else:
            print('Not a palindrome')
            break
    else:
        print('Is a palindrome')


a=str(input('enter the string:'))
fun_pal(a)'''

#Method-2

'''def fun_pal(c):
    b=c[::-1]
    if b==c:
        print('P')
    else:
        print('Not P')

a=str(input('enter the string:'))
fun_pal(a)'''

#Questioon-4

'''def prime(a):
    
    for i in range(2,a//2,1):
        if(a==1 or a==2):
            print('True')
            break
        if a%i==0:
            print('False')
            break
        else:
            continue
    else:
        print('True')


a=int(input('enter the number:'))
prime(a)
'''

#Question-5

'''def check(l):
    c=''
    for i in range(1,len(l),2):
        c=c+a[i]
    return c

a=str(input('enter the string:'))
print(check(a))'''

#Question-6

'''def dic(l):
    for key,value in l.items():
        print(key,end=" ")

a={x:(x**2) for x in range(1,11)}
dic(a)'''

#Question-7

'''def dic1(l):
    for key,values in l.items():
        if values==100:
            print(key)

a={x:(x**2) for x in range(1,11)}
dic1(a)'''

#Question-8

'''def check2(l):
    for i in l:
        if i.count('s')==2:
            print(i)
a=list(map(str,input('enter the string:').split()))
check2(a)'''

#Question-9

'''def idch(a):
    for i in a:
        for key,values in i.items():
            if key=='id':
                print(i)
                break

a=[{'id':1001,'name':'harsh','sal':70000},{'id':1002,'name':'Sid','sal':60000},{'name':'Piyush','sal':200000}]
idch(a)'''

#************************************************************************************************************************
#                                             Function - practice

#Question-1

'''def max(a,b,c):
    max=a
    if a>b and a>c:
        max=a
    elif b>a and b>c:
        max=b
    else:
        max=c
    return max
a,b,c=map(int,input('enter the numbers').split(' '))
print(max(a,b,c))'''


#Question-2

'''def sum(l):
    sum=0
    for i in  l:
        sum+=i
    return sum
a=list(map(int,input('enter the list').split(" ")))
print(sum(a))'''


#Question-3


'''def mul(l):
    mul=1
    for i in  l:
        mul*=i
    return mul
a=list(map(int,input('enter the list').split(" ")))
print(mul(a))'''

#Question-4

'''def rev(a):
    b=a[::-1]
    return b
a=str(input('enter the string:'))
print(rev(a))'''

#Question-5

'''def fact(a):
    c=1
    for i in range(1,a+1,1):
        c*=i
    print(c)
a=int(input('enter the number:'))
fact(a)'''

#Question-6


'''def fun(p,q,r):
    if p in range(q,r+1,1):
        print("Yes")
    else:
        print('No')
    
a=int(input('enter the number:'))
b,c=map(int,input('enter the range:').split(' '))
fun(a,b,c)'''

#Question-7

'''def fun(l):
    c=0
    d=0
    for i in range(len(l)):
        if l[i].islower():
            c+=1
        if l[i].isupper():
            d+=1
    print('Lower case:',c)
    print('Upper case:',d)
a=str(input('enter the string:'))
fun(a)'''

#Question-8

'''def che(a):
    b=set(a)
    print(list(b))
a=list(map(int,input('enter the numbers:').split()))
che(a)'''

#Question-9


'''def prime(a):
    
    for i in range(2,a//2,1):
        if(a==1 or a==2):
            print('True')
            break
        if a%i==0:
            print('False')
            break
        else:
            continue
    else:
        print('True')


a=int(input('enter the number:'))
prime(a)
'''

#Question-10

'''def even(l):
    b=[]
    for i in l:
        if i%2==0:
            b.append(i)
    return b


a=list(map(int,input('enter the list').split(',')))
print(even(a))'''

#Question-11

'''def perfect(l):
    sum=0
    for i in range(1,l,1):
        if l%i==0:
            sum+=i
    if sum//2==l//2:
        print('perfect divisor')
    else:
        print('not a perfect divisor')

a=int(input('enter the number:'))
perfect(a)'''

#Question-12


'''def fun_pal(c):

    for i in range(len(c)):
        if a[i]==a[-i-1]:
            continue
        else:
            print('Not a palindrome')
            break
    else:
        print('Is a palindrome')


a=str(input('enter the string:'))
a.replace(" ","")
fun_pal(a)'''

#Question-13

#Question-14

'''def pang(l):
    l=l.lower()
    l=l.replace(" ",'')
    b = list(l)
    e= set(b)

    b=list(e)
    b.sort()
    c="".join(b)
    print(c)
    if c =='abcdefghijklmnopqrstuvwxyz':
        print('pangram')

a=str(input('enter the string:'))
pang(a)'''

#Question-15

'''def sor(b):
    a=b.split('-')
    a.sort()
    print("-".join(a))


a=list(map(str,input('enter the str:').split('-')))
b="-".join(a)
sor(b)
'''

#Question-16

'''def fun(a):
    a=[e**2 for e in range(1,a+1)]
    print(a)

a=int(input('enter the number:'))
fun(a)'''

#Question-17
