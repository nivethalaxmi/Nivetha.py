#palindrome

n=input("Enter the string :")
m=""
for i in n:
    m=i+m
print(m)
if(n==m):
    print("true")
else:
    print("false")
    
#vowels
n="education"
count=0
for i in n:
    if i in "aeiouAEIOU":
        count+=1
print(n)
print("No.of.Volwels:",count)

#Reverse string
word="Nivetha"
m=''
for i in word:
    m=i+m
print(m)

#count the upper/lower
string='UpperCase and LOWERcase'
ucount=0
lcount=0
for i in string:
    if(i>="A" and i<="Z"):
        ucount+=1
    elif(i>="a" and i<="z"):
        lcount+=1
print(ucount)
print(lcount)

#Duplicate character
n="Programming"
t=""
for i in n:
    if i not in t:
        t=t+i
print(t)

n="programming"
t=""
f=""
for i in n:
    if i  not in t:
        t=t+i
    else:
        f=f+i
        
print(f)

#anagrams
string1=input("Enter the String")
string2=input("Enter the string")
if(sorted(string1)==sorted(string2)):
    print('true')
else:
    print('false')
    
#remove all alphabetic characters
s=input()
temp=""
for i in s:
    if(i>="A" and i<="Z" or i>="a" and i<="z"):
        temp=i+temp
print(temp)
        

#countString
S=input()
count=0
temp=""
for i in S:
    temp=i+temp
    count+=1
print(temp)
print(count)


#sum of all digit
d=input()
sum=0
for i in d:
    if i in "123456789":
        sum=sum+int(i)
print(sum)

##Replacce all lspaces
s="Hello World"
j=s.split(" ")
j2="-".join(j)
print(j2)

#Capitalize the first letter
s=input()
print(s.title())

#Extract every second character from string
s=input()
print(s[::2])

#startwith/endwith
s=input()
print(s.startswith("we"))
print(s.endswith("ma"))



























    










