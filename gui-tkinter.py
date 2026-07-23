import tkinter as tk
from tkinter import messagebox
def sp(pg):
    pg.tkraise()
def register():
    print(reg_name.get())
    print(reg_EmailID.get())
    print(reg_MobileNuber.get())
    print(reg_Password.get())
    messagebox.showinfo("Register","Register is succesfully")
def login():
    print(reg_EmailID.get())
    print(reg_Password.get())
    messagebox.showinfo("Login","Login is succesfully")
    ds.tkraise()






main=tk.Tk()
main.geometry('1366x768')
main.title("E-Commerce Webiste")
main.config(background="#582f0e")
#frame
container=tk.Frame(main,bg="#132a13")
rg=tk.Frame(container,bg="#31572c")
lg=tk.Frame(container,bg="#936639")
ds=tk.Frame(container,bg="#6f1d1b")
for page in (container,rg,lg,ds):
    page.place(x=0,y=0,width=1366,height=768)
#rg

tile=tk.Label(rg,text='Welcome to E-comerce Website',bg="#31572c",fg="#432818",font=("Times New Roman",33,"bold"))
tile.place(x=350,y=80)
subtite=tk.Label(rg,text="Register Login",bg="#31572c",fg="#333d29",font=("Time New Roman",22,"bold"))
subtite.place(x=520,y=180)

tk.Label(rg,text="UserName",bg="#31572c",fg="#03071e",font=("Arial bold",18)).place(x=350,y=300)
reg_name=tk.Entry(rg,bg="#31572c",fg="#03071e",font=("Arial bold",25),width=16)
reg_name.place(x=600,y=300)
tk.Label(rg,text="EmailID",bg="#31572c",fg="#03071e",font=("Arial bold",18)).place(x=350,y=350)
reg_EmailID=tk.Entry(rg,bg="#31572c",fg="#03071e",font=("Arial bold",25),width=16)
reg_EmailID.place(x=600,y=350)


tk.Label(rg,text="MoblieNumber",bg="#31572c",fg="#03071e",font=("Arial bold",18)).place(x=350,y=400)
reg_MobileNuber=tk.Entry(rg,bg="#31572c",fg="#03071e",font=("Arial bold",25),width=16)
reg_MobileNuber.place(x=600,y=400)
tk.Label(rg,text="Password",bg="#31572c",fg="#03071e",font=("Arial bold",18)).place(x=350,y=450)
reg_Password=tk.Entry(rg,bg="#31572c",fg="#03071e",font=("Arial bold",25),width=16)
reg_Password.place(x=600,y=450)
tk.Button(rg,bg="#582f0e",fg="#606c38",font=("Arial bold",15),text="Login Form",command=lambda:sp(lg)).place(x=500,y=550)
tk.Button(rg,bg="#582f0e",fg="#606c38",font=("Arial bold",15),text="Register",command="Register").place(x=660,y=550)

#login page
tile=tk.Label(lg,text='LOGIN USER',bg="#936639",fg="#432818",font=("Times New Roman",33,"bold"))
tile.place(x=500,y=80)
tk.Label(lg,text="EmailID : ",bg="#936639",fg="#03071e",font=("Arial bold",18)).place(x=450,y=200)
reg_EmailID=tk.Entry(lg,bg="#936639",fg="#03071e",font=("Arial bold",25),width=16)
reg_EmailID.place(x=600,y=200)
tk.Label(lg,text="Password : ",bg="#936639",fg="#03071e",font=("Arial bold",18)).place(x=450,y=300)
reg_Password=tk.Entry(lg,bg="#936639",fg="#03071e",font=("Arial bold",25),width=16)

reg_Password.place(x=600,y=300)
tk.Button(lg,bg="#582f0e",fg="#606c38",font=("Arial bold",15),text="Register",command=lambda:sp(lg)).place(x=550,y=450)
tk.Button(lg,bg="#582f0e",fg="#606c38",font=("Arial bold",15),text="Login Form",command=login).place(x=700,y=450)









rg.tkraise()
main.mainloop()