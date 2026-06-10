#syp number
num=int(input())#12
b=0#3
p=1
temp=num#12
while(temp>0):
    d=temp%10#2
    b+=d#5
    p*=d
    temp=temp//10
if(b==p):
    print("it is syp number")
else:
    print("its not a syp number")

#special number
num=int(input())
b=0
p=1
temp=num
while(temp>0):
    d=temp%10
    b+=d
    p*=d
    temp=temp//10
if(b+p==num):
    print("it is special number")
else:
    print("it is  not special number")
    
#Harshard number
num=int(input())
b=0
temp=num
while(temp>0):
    d=temp%10
    b+=d
    temp=temp//10
if(num%b==0):
    print("it is harshard number")
else:
    print("its not a harshared number")

#count of digits
num=int(input("enter the number"))
count=len(str(num))
print("no.of.digits",count)


#split and square of digit
num=int(input())
temp=num
while(temp>0):
    d=temp%10
    seq=d*d
    print(d,"square",seq)
    temp=temp//10
#sum of digits

num=int(input("Enter the digit"))
b=0
temp=num
while temp>0:
    digit=temp%10
    b+=digit
    temp=temp//10
print(b)
    
#count the digit
count=0
num=int(input("Enter the digit"))
temp=num
while temp>0:
    temp=temp//10
    count+=1
print(count)

#product of number
num=int(input())
p=1
temp=num
while temp>0:
    d=temp%10
    p*=d
    temp=temp//10
print(p)

#odd/even
num=int(input())
oddsum=0
evensum=0
while num>0:
    d=num%10
    if(d%2==0):
        evensum+=d#2
    else:
        oddsum+=d#3#1
    num=num//10
print("evendigit",evensum)
print("odddigit",oddsum)

#count the digit
count=0
num=int(input("Enter the number"))

while(num>0):
    d=num%10
    
    if(d==2 or d==3 or d==5 or d==7):
        count+=1
    num=num//10
print(count)

#palindrome
num=int(input())
temp=num
b=0
while temp>0:
    d=temp%10
    b=b*10+d
    temp=temp//10
if(b==num):
    print("its palindrome")
else:
    print("it is not a palinodrome")
#neon number
num=int(input())
temp=num*num
b=0

while temp>0:
    d=temp%10
    b+=d
    temp=temp//10
if(b==num):
    print("its palindrome")
else:
    print("it is not a palinodrome")

#duck number
num=(input())
if('0' in num and num[0]!='0'):
    print("duck number")
else:
    print("its not duck number")
#automorphic number
num=int(input())
squ=num*num
if(str(squ).endswith(str(num))):
    print("automorphic number")
else:
    print("its not a automorphic numberr")

#armstrong number
num=int(input())
temp=num
b=0
n=len(str(num))
while temp>0:
    d=temp%10
    b+=d**n
    temp=temp//10
if(num==b):
    print("it is armstrong number")
else:
    print("it is not a armstrong number")

#strong number

num=int(input())
temp=num
sum=0
while temp>0:
    digit=temp%10
    f=1
    for i in range(1,digit+1):
        f*=i
    sum+=f
    temp=temp//10
if(sum==num):
    print("strong number")
else:
    print("not a strong number")


#perfect number
num=int(input())
sum=0
for i in range(1,num):
    if(num%i==0):
        sum+=i
print(sum)
if(num==sum):
    print("perfect number")
else:
    print("not a perfect number")
#happy number
num=int(input())
temp=num
while temp!=1 and temp!=4:
    b=0
    while(temp>0):
        d=temp%10
        b+=d*d
        temp=temp//10
    temp=b
if(temp==1):
    print("happy number")
else:
    print("not a happy number")

#factorial number
num=int(input())
f=1
i=1
while i<=num:
    f=f*i
    i+=1
print(f)
    
#revese number
num=int(input())
temp=num
b=0
while temp>0:
    d=temp%10
    b=d
    print(b,end="")
    temp=temp//10

    
























    

















































    
    
    




