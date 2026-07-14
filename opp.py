from encodings import gbk
from webbrowser import GenericBrowser


class Mobile:
    Brand = None
    Model = None
    Color = None
    Price = None
    def power_on(self):
        print("power on",self.Brand)
mobile1=Mobile()
mobile1.Brand="OPPO"
mobile1.Mobel="A78"
mobile1.Color="Bule"
mobile1.Price=100
print(mobile1.Brand)
print(mobile1.Model)
print(mobile1.Color)
print(mobile1.Price)
mobile1.power_on()
class Laptop:
    Brand=None
    Processor=None
    RAM=None
    Price=None
    def start(self):
        print("Start the laptop",self.Brand)
L1=Laptop()
L1.Brand="Acer"
L1.Processor="5 or Amd Ryzen"
L1.RAM="8GB"
L1.Price=500000
print("Brand :",L1.Brand)
print("Processor :",L1.Processor)
print("RAM :",L1.RAM)
print("Price :",L1.Price)
L1.start()

class student():
    Name=None
    RollNo =None
    Email=None
    Mark=None
    def display(self):
        print("Enter you marks:",self.Mark)
stu=student()
stu.Name="Nivetha"
stu.rollNo="123"
stu.Email="nivethalakshmi0810@gmail.com"
stu.Mark=897
print("Name :",stu.Name)
print("RollNo :",stu.RollNo)
print("Email :",stu.Email)
print("Mark :",stu.Mark)
stu.display()

class Car():
    Brand=None
    model =None
    Color=None
    def drive(self):
        print("Display the detial ")
c1=Car()
c1.Brand="TATA"
c1.model="123"
c1.color="Black"
print("Brand :",c1.Brand)
print("model :",c1.model)
print("color :",c1.color)
c1.drive()

class book():
    Tilte=None
    Author =None
    Price=None
    def read(self):
        print("read the book")
b1=book()
b1.Tilte="programing language"
b1.price="500"
b1.Author="Nivetha"

print("Title :",b1.Tilte)
print("Price :",b1.price)
print("Author :",b1.Author)
b1.read()

class Fan():
    Band=None
    Speed =None
    Color=None
    def rotate(self):
        print("Display the fan")
f1=Fan()
f1.Brand="celling fan"
f1.Speed="200"
f1.Color="brown"
f1.rotate()
print("Brand:",f1.Brand)
print("Speed :",f1.Speed)
print("Color:",f1.Color)

class tv():
    Band=None
    size =None
    Color=None
    def switch_on(self):
        print("Display the fan")
t1=tv()
t1.Brand="sony"
t1.size="55 in"
t1.Color="brown"
t1.switch_on()
print("Brand:",t1.Brand)
print("Speed :",t1.size)
print("Color:",t1.Color)

class Bike():
    Band=None
    Model =None
    Mieage=None
    def ride(self):
        print("Display the fan")
b1=Bike()
b1.Brand="tvs"
b1.model="55 in"
b1.Mieage="brown"
b1.ride()
print("Brand:",b1.Brand)
print("Mieage:",b1.Mieage)
print("Model :",b1.Model)

class Employee():
    Name=None
    ID=None
    Salary=None
    def work(self):
        print("Display the emplyeee")
e1=Employee()
e1.Name="Ram"
e1.ID="23456"
e1.Salary="25000"
e1.work()
print("Brand:",e1.Name)
print("Speed :",e1.ID)
print("Color:",e1.Salary)

class BankAccount():
    AccountNo=None
    holder=None
    Name=None
    balance=None
    def Check_balance(self):
        print("Display the emplyeee")
a1=BankAccount()
a1.AccountNo="12314556"
a1.ID="23456"
a1.holder="female"
a1.Name="Nivetha"
a1.balance=1000
a1.Check_balance()
print("AccountNo:",a1.AccountNo)
print("ID :",a1.ID)
print("Holder:",a1.holder)
print("Balance:",a1.balance)


