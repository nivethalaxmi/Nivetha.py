#1.Find the length
s=input("Enter the text: ")
count=0
for i in s:
    count+=1
print("total length of string",count)

#2.Check string contains only alphabet
s=input("Enter the string")
if s.isalpha():
    print("True")
else:
    print("False")

#3.Check string contains only digits
d=input("Enter the digit")
if d.isdigit():
    print("it only contain digits")
else:
    print("not only digits")

#4.Count the number of consonants
string=input("Enter the string")
count=0
for i in string:
    if i not in "AEIOUaeiou":
        count=count+1
print(count)

#5.First non-repeating character
string=input("Enter the string")
count={}
for i in string:
    count[i]=count.get(i,0)+1
for i in string:
    if(count[i]==1):
        print("non repeating chaaracter is: ",i)
        break
#6.Swapcase the character
string=input("Enter the string")
s1=string.swapcase()
print(s1)

#7.Remove the all space from the string
string=input("Enter the String")
string=string.replace(" ","")
for i in string:
    print(i,end="")
    
#8.check if string start with a vowel
string=input("Enter the string")
if string.isalpha():
    if string[0]in "AEIOUaeiou":
        print("its is true")
    else:
        print("its is false")
        
#9.count occurrence of a character
string=input("Enter the string")
ch=input("Enter the character")
count=0
for i in string:
    if i==ch:
        count=count+1
print(count)
    
#10.Replace all vowles with *
string=input("Enter the string")
for i in string:
    if i in "AEIOUaeiou":
        string=string.replace(i,"*")
print(string)

#11.even index postition
s=input("Enter the string")
for i in range(len(s)):
    if (i%2==0):
        print(s[i],end="")
        
#12.odd index postition
s=input("Enter the string")
for i in range(len(s)):
    if (i%2!=0):
        print(s[i],end="")
        
#13.convert string to list
s=input("Enter the string")
s1=list(s)
print(s1)

#14.special charater    
s=input("Enter the string")
count=0
for i in s:
    if not i.isalpha()and  not i.isdigit()and  not i.isdecimal() :
        count=count+1
print(count)

#15.check both letter and numbers
s=input("Enter the string")
if s.isalnum():
    print("its true")
else:
    print("false")

#16.Remove the leading ,trailing spaces
s="  hello  "
s1=""
start=0
end=len(s)-1
while start<=end and s[start].isspace():
    start+=1
while end>=start and s[end].isspace():
    end-=1
for i in range(start,end+1):
    s1+=s[i]
print(s1)

#17.ASCII value
s=input("Enter the string")
for i in s:
    print(i,ord(i))
    
#18.longest word
s=input("Enter the string")
w=s.split()
l=""
for w in w:
    if(len(w)>len(l)):
       l=w
print(l)
#19.split the string
s=input()
w=""
for i in s:
    if i==" ":
        print(w)
        w=""
    else:
        w+=i
print(w)

#20.valid identifier
s=input("Enter the string")
s1=s.isidentifier()
print(s1)







































































            
