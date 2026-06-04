
#task1
m=int(input("Enter the m value"))
n=int(input("Enter the n value"))
if(m>n):
    print("quotient",m//n)
    print("remainder",m%n)
else:
    print( "invild number")'

#task2
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
marks=a+b+c+d+e
if(marks>=490):
    print("grade a+")
elif(marks >=480):
    print("grade a")
elif(marks >=370):
    print("grade b+")
elif(marks>=360):
    print("grade b")
elif(marks>=250):
    print("grade c")
elif(marks<240):
    print("fail")
else:
    ("invalid mark")

#task 3
num=int(input())
if(num>0):
    print(num,"is positive number")
elif(num<0):
    print(num,"is negative number")
else:
    print( num,"is zero")''
#eve/odd
num=int(input("Enter the number"))
if(num%2==0):
    print(num,"is even number")
else:
    print(num,"is odd number")''
#pass/fail
mark=int(input("Enter the mark"))
if(mark>=50):
    print("you are pass")
else:
    print("you are fail")'
#leap year
year=int(input("enter the year"))
if(year%4==0):
    print("leap year")
else:
    print("not a leap year")


#task4
x=input()
if(x=='a' or x=='e' or x=='i' or x=='o' or x=='u'):
    print(" it's vowels")
else:
    print(" it's consonants")

 
#task5
a=int(input())
b=int(input())
c=int(input())
if(a>b and a>c):
    if(b>a and b>c):
        print(b)
    else:
        print(a)
else:
    print(c)

#task6
ses=input("Enter the month")
if(ses == "march" or ses == "april" or ses == "may"):
    print("its is spring")
elif(ses=="june" or ses=="july" or ses=="august" ):
    print("its is summer")
elif(ses=="september" or ses=="october" or ses=="november"):
    print("its is autumn")
elif(ses=="december" or ses=="january" or ses=="february"):
    print("its is winter")
else:
    print("enter the corect month")
    
#task7
days=input("Enter the month")
if(days=="jan" or days=="march" or days=="may" or days=="july" or days=="august" or days=="octobar" or days=="dec"):
    print(days," has 31 days")
elif(days=="april" or days=="june" or days=="september" or days=="novermber"):
    print(days,"has 30 days")
else:
    print(days,"has 28 days")'

#task8
a=int(input("Enter the number"))
if(a%5==0):
    print("Hello")
else:
    print("bye")

    
#task9
degree=int(input())
if(degree>=70):
    print("its boiling ")
else:
    print("it is not")


    
 #task10
charge=int(input("Enter the value"))
if(charge>=1 and charge<=5):
    print("book charge:",charge*2)
elif(charge>=6 and charge<=10):
    print("book charge:",charge*3)
elif(chrge>=11 and charge<=15):
    print("book charge:",charge*4)
elif(charge>=16):
    print("Book charge:",d*5)
else:
    print("invaild number")

#task11
age=int(input("Enter the age"))
if(age>=25 and age<=50):
    print("eligible to work in police")
else:
    print("not eligible to work in police")'

#task12
b=int(input("Enter the salary"))
if(b>=12000 and b<=15000):
    print("employee bonus is:",b+3000)
elif(b>=20000 and b<=25000):
    print("employee bonus is :",b+5000)
else:
    print(" employee are fresher no bonus")

#task 13
units=int(input("Enter the electric units"))
if(units>=900 and units<1500):
    print(" your electric unit bill is 1120")
elif(units>=1500 and units<2200):
    print("your electric unit bill is 3000")
else:
    print("you has no elecity bill")


#task14
password= int(input("Enter the password"))
if(password==12345):
    print("succesfull login")
else:
    print("enter wrong password")










































    




















