#1sum of list
s=["apple",23,45,77,99]
s1=0
for i in s:
    s1=s1+1
print(s1)

#2.largest number    
s=[99,344,77,455,77]
s1=s[0]
for i in s:
    if i>s1:
        s1=i
print("largest number",s1)

#3.smallest number
s=[34,76,89,82,55]
s1=s[0]
for i in s:
    if i<s1:
        s1=i
print("smallest number",s1)

#4.remove the duplicate
s=["apple",32,"banana",87,32]
s1=[]
for i in s:
    if i not in s1:
        s1.append(i)
print("list without duplicate is :",s1)

#5.copy list
s=["apple",32,"banana",87,32]
s2=s.copy()
print(s2)

s=["apple","banana","true" ,"salem"]
#6.reverse list
s1=[]
for i in s:
    s1.insert(0,i)
print(s1)
#2nd method
s=["apple","banana","true" ,"salem"]
s.reverse()
print(s)
#7.different data typr
l=['apple',23,'hello',98,90,40]
print(l)

#8.remove the empty element form list
l=[48,"hello",90," ",45,"world"," "]
m=[]
for i in l:
    if i!=" ":
        m.append(i)
print(m)

#9.append all element in list to second list
l2=["apple","banana","true" ,"salem"]
l2.append(l)
print(l2)

#10.select random item
l2=["apple","banana","true" ,"salem",'hello']
print(l2[2:4])

#11.odd/even
l=[32,22,7,2,9,8,12,5,77]
e=[]
o=[]
for i in l:
    if  i%2==0:
        e.append(i)
    else:
        o.append(i)
print(e,"even")
print(o,"odd")
#12.ascending order
s=[32,22,77,6,19,78,55,48]
s.sort ()
print(s)

#13.decending order
s=[32,22,77,6,19,78,55,48]
s.sort(reverse =  True)
print(s)

#14.count element in list
s=[32,22,77,6,19,78,55,48]
count=0
for i in s:
    count+=1
print(count)
s1=len(s)
print(s1)

#15.average number
s=[32,22,77,6,19,78,55,48]
count=0
sum=0
for i in s:
    sum+=i
    count+=1
    av=sum/count
print(sum)
print(count)
print(av)

 #count specific element in list   
s=[32,22,77,6,19,78,55,78,77]
s1=[]
s2=[]
for i in s:
    if i not in s1:
        s1.append(i)
    else:
        s2.append(i)
        count=len(s2)
print(s2)
print(count)
    
#17.element is exit/not
s=[32,22,77,6,19,78,55,78,77]
s1=32
if s1 in s:
    print("its is exit")
else:
    print("not exit")
    
#18.insert
s=[32,22,77,6,19,78,55,78,77]
s.insert(2,"apple")
print(s)

#19.remove
s.remove(55)
print(s)

#20.seecond largest number
s=[32,22,77,6,19,78,55]
max=0
max2=0
for i in s:
    if i > max:
        max2=max
        max=i
    elif i > max2:
        max2=i
print(max2)

#21.merge list
s=[32,22,77,6,19,78,55]
l=["apple","banana","true" ,"salem",'hello']
for i in l:
    s.append(i)
print(s)
#2nd method
merge=s+l
print(merge)

#22.Find the common b/w 2 list
s=[32,22,77,6,19,78,55,"apple"]
l=["apple","banana","true" ,"salem",'hello']
merge=s+l
l2=[]
l3=[]
for i in merge:
    if i not in l2:
        l2.append(i)
    else:
    
        l3.append(i)
print(l3)
          
#23.positive numbr
n=[9,8,7,-7,-4,3,98,-88]
n1=[]
for i in n:
    if i>0:
        n1.append(i)
print("positive number",n1)

#24.replace the negative number into zero
n=[9,8,7,-7,-4,3,98,-88]

for i in range len(n)):
    if n[i]<0:
       n[i]=0 
print("positive number",n)

 #25.index  position       
l=["apple","banana","true" ,"salem",'hello']
print(l.index("apple"))

#26. store 5 student name
name=["nivetha","saarah","oviya","pavi","fathima"]
for i in name:
    print(i)
    
#27.store 10 markk max/min
num=[34,88,21,99,67,23,81]
print("max",max(num))
print("min",min(num))
#2nd method
max=num[0]
min=num[0]
for i in num:
    if i>max:
        max=i
    elif i<min:
        min=i
print(max)
print(min)

#29.store employee slaries
n=int(input("Enter the products:"))
p=[]
t=0
for i in range(n):
    p1=float(input(f"Enter the price of the product{i+1}:"))
    p.append(p1)
for p1 in p:
    t=t+p1
print(p)
print(t)


r=[23000,45000,34000,77000,13000]
for r in r:
    if r>25000:
        print(r)
        
#30.present/absent
n=int(input("Enterr the student"))
n1=[]
pc=0
ac=0
for i in range(n):
    n2=input(f"Enter the {i+n} student is p/a:")
    n1.append(n2)
for n2 in n1:
    if n2=="p":
        pc+=1
    else:
        ac+=1
print(n1)
print(pc)
print(ac)
    























































































