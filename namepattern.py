n=6
for i in range(n):
    for j in range(n):
        if(j==0 or j==5 or i==j):
            print("*",end="")
        else:
            print(" ",end="")
    print(end=" ")
        
    for j in range(n):
        if(j==3 or i==0 or i==5 ):
            print("*",end="")
        else:
            print(" ",end="")
    print(end=" ")
    for j in range(n):
        if(j==i ):
            print("*",end="")
        else:
            print(" ",end="")
    print(end=" ")
    
    for j in range(n):
        if(5==j+i):
            print("*",end="")
        else:
            print(" ",end="")
    print(end=" ")
    
    for j in range(n):
        if(j==0 or i==0 or i==5 or i==3):
            print("*",end="")
        else:
            print(" ",end="")
    print(end=" ")
        

    for j in range(n):
        if( i==0 or  j==3):
            print("*",end="")
        else:
            print(" ",end="")
    print(end=" ")
    
    for j in range(n):
        if( j==0 or  j==5 or i==3):
            print("*",end="")
        else:
            print(" ",end="")
    print(end=" ")
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        if(i==3 or j==0   or j==n):
             print("*",end="")
        else:
            print(" ",end="")
    
    for j in range(i+1):
        if( i==3 or  j==i or j==n):
             print("*",end="")
        else:
            print(" ",end="")
    print()












