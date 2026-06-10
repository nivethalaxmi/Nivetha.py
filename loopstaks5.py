#factorial number
i=5
f=1
while(i>0):
    f=f*i
    i-=1
print(f)

#natural number
#while loop
i=1
while(i<=10):
    print(i)
    i+=1
#for loop
for i in range(1,11):
    print(i)
    
#sum
i=1
sum=0
while(i<=10):
    sum+=i
    i+=1
print(sum)

#fibonacci sseries
n1=0
n2=1
for i in range(6):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
    
#hcf for two number
n1=int(input("Enter the num1:"))
n2=int(input("Enter the num2:"))
hcf=1
for i in range(1,min(n1,n2)+1):
    if(n1%i==0 and n2%i==0):
        hcf=i
print("Hcf is ",hcf)

#multiplication table:
n=int(input("Enter the number"))
for i in range(1,10+1):
    print(i,"x",n,"=",i*n)
    
#palindrome
a=151
rev=0
c=a
while c>0:
    d=c%10
    rev=rev*10+d
    c=c//10
if(rev==a):
    print(f"{rev} is palindrome")
else:
    print(f"{rev} not a palindrome")
    
#armstrong number
a=int(input())
b=0
c=a
n=len(str(a))
while (c>0):
    d=c%10
    b+=d**n
    c=c//10
if(b==a):
    print(" is armstrong number")
else:
    print("is not  armstrong number")

#task9
for i in range(1,51):
    if(i%3==0):
        print(i,"Hi")
    elif(i%5==0):
        print(i,"hello")
    elif(i%3==0 and i%5==0):
        print(i,"hihello")
    
#prime number
num=int(input())
if num>1:
    for i in range(2,num):
        if(num%i==0):   
            print("its not  prime number")
            break
    else:
            print("its is a prime number")
else:
    print("its is not a primenumber")
        
#prime number count
count=0
for i in range(0,101):
    if (num>1):
        for j in range(2,num):
            if(i%j==0):
                break
        else:
            print(i)
            count+=1

print("total number of prime number:",count)

#positive divisor
num=int(input())
for i in range(1,num+1):
    if(num%i==0):
        print(i)
        
#odd/even
num=int(input())
oddsum=0
evensum=0
for i in range(1,num+1):
    if(i%2==0):
        evensum+=i
    else:
        oddsum+=i
print(evensum)
print(oddsum)

#square number
num=int(input())
for i in range(1):
    seq=num*num
print(seq)
                




















    




      
