
#increment triangle
for i in range(5):
    for j in  range(i+1):
        print(j+1,end="")
    print()
#decement triangle
for i in range(5):
    for j in range(i,5):
        print("*",end="")
    print()
#increment triangle   
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()
    
# Right-Angled Triangle Pattern
#increment
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()
#Inverted Right_Angled Triangle
for i in range(5):
    for j in range(i,5):
        print("*",end="")
    print()

#Pyramid Pattern
for i in range(5):
    for j in range(i,5):
        print(" ",end="")
    
    for j in range(i+1):
        print("*",end="")
    
    for j in range(i):
        print("*",end="")
    print()

#inverted Pyranid

n=7
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print("*",end="")
    for j in range(i,n-1):
        print("*",end="")
    print()

#Diamond Pattern
n=7
for i in range (n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    for j in range(i):
        print("*",end="")
    print()

for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print("*",end="")
    for j in range(i,n-1):
        print("*",end="")
    print()



#hollow Pattern

for i in range(5):
    for j in range(5):
        print(j,end="")
    print()

#hollow square pattern
n=5
for i in range(n):
    for j in range(n):
        if(i==0 or i==4 or j==0 or j==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()

#Hollow Right triangle pattern
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        if i==j or j==1 or i==n:
            print("*",end="")
        else:
            print(" ",end="")
        
       
    print()
#hollow  Right triangle
n=5
for i in range (n):
    for j in range(i+1):
        if(i==0 or i==n or i==4 or j==0 or j==n or i==j):
            print("*",end="")
        else:
            print(" ",end="")
    print()

    
#hollow inverter  Right triangle
n=5
for i in range (n):
    for j in range (i,n):
        if(i==n or i==0 or j==n or j==4 or i==j):
            print("*",end="")
        else:
            print(" ",end="")

    print()
#Hollow pyramid pattern
n=5
for i in range (n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        if(i==4  or j==0   or j==n):
             print("*",end="")
        else:
            print(" ",end="")
    
    for j in range(i+1):
        if(i==4    or j==i or j==n):
             print("*",end="")
        else:
            print(" ",end="")
    print()
    
#hollow inverted pyramid pattern
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        if(i==0   or i==j ):
            print("*",end="")
        else:
            print(" ",end="")
    for j in range(i,n-1):
        if(i==0 or j==3  ):
            print("*",end="")
        else:
            print(" ",end="")
        
    print()

#plus pattern
n=5
for i in range (n):
    for j in range (n):
        if(i==2 or j==2 ):
            print("*",end="")
        
        else:
            print(" ",end="")
    print()
      
            

words="apple"
n=5
for i in range (n):
    for j in range (n):
        if(i==2 ):
            print(words[j] ,end="" )
        elif(j==2):
            print(words[i],end="")
        
        else:
            print(" ",end="")
    print()
    
words="apple"      
n=5
for i in range(n):
    for j in range(n):
        if(4==i+j ):
            print(words[j],end="")
        elif(i==j):
            print(words[i],end="")
            
        else:
            print(" ",end="")
    print()

#hollow inside char pattern       
n=5
c=122
for i in range(n):
    for j in range(n):
        if(i==0 or i==4 or j==0 or j==4):
            print("*",end="")
        else:
            print(chr(c),end="")
            c-=1
            
            
    print()


#whileloop
#1increment
i=10
while(i<=200):
    print(i)
    i+=10

#2
i=10
while (i>0):
    print(i)
    i-=1
#3 factorial number
i=5
f=1
while(i>0):
    f=f*i
    i-=1
print(f)

#4 increment even number
i=2
while(i<=20):
    print(i)
    i+=2
#5 odd number
i=1
while(i<=20):
    print(i)
    i+=2
#square number
i=1
while(i<=5):
    print(i*i)
    i+=1
#decrement
n=10
while(n>=1):
    print(n)
    n-=1

i=5
while(i>=1):
    print(i)
    i-=1
#even number
i=20
while(i>=2):
    print(i)
    i-=2

#multiplication table
i=1
while(i<=10):
    print(i,"x7=",i*7)
    i+=1








    

    
























    
































