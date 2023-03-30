from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from time import*
import tkinter as tk

import pymysql

db=pymysql.Connection(host="localhost",user="root",password="12345",database='bank')#,database="newat5")
cur=db.cursor()
cur.execute("use bank")
# main balance
bal=40000
###################################
def clicked():
    clicked1=Tk()
    global amount_deposited_succussfully,thank_you,w9
    messagebox.showinfo("amount depostited successfully")
    b=Button(clicked1, text = "OK" , command = thank_you)
    b.grid(column=1,row=1)
    thank_you()

#add()
def add():
    global bal, data,clicked
    data=int(e3.get())
    bal+=data
    print("After deposit:",bal)
    clicked()
    
#widhdrawelclick()
def widhdrawelclick():
    global sub,widhdrawelclick
    widhdrawelclick1=Tk()
    messagebox.showinfo("amount depostited successfully")
    b=Button(widhdrawelclick1, text = "OK" , command = widhdrawelclick)
    b.grid(column=1,row=1)
    thank_you()
    
#sub()
def sub():
    global bal,data1
    data1=int(e4.get())
    bal-=data1
    print("After withdrewl",bal)
    widhdrawelclick()
####################################################################

welcome=tk.Tk()
#geomentry
welcome.title("ATM")
welcome.geometry("{0}x{1}+0+0".format(welcome.winfo_screenwidth(), welcome.winfo_screenheight()))

# #canvaas
c = Canvas(welcome, width=1366, height=768, bg='lawn green')
c.grid(row=0, column=0)
#welcome image
image = Image.open("pj3.jpg")
image = image.resize((welcome.winfo_screenwidth(), welcome.winfo_screenheight()), resample=Image.LANCZOS)

photo = ImageTk.PhotoImage(image)

labelle = tk.Label(welcome, image=photo)
labelle.place(x=0, y=0, relwidth=1, relheight=1)

#welcome label
labelwel=Label(welcome,text="WELCOME TO INDIAN BANK ",fg="Yellow",bg="dark blue",font="verdana 35 bold")
labelwel.place(x=300,y=270)
#welcome get started buttion

def root():
    root=Tk()
    global photo,imgroot,photoroot,name,mail,phoneno,pwd,paas,accountno
    #geomentry
    root.title("ATM")
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

    # #canvaas
    c = Canvas(root, width=1366, height=768, bg='lawn green')
    c.grid(row=0, column=0)
    #img
    # image = ImageTk.PhotoImage(Image.open("pj3.jpg",'r'))  # PIL solution
    # #resize
    # image = image.resize((root.winfo_screenwidth(1366), root.winfo_screenheight(768)), Image.ANTIALIAS)
    # c.create_image(0, 0, anchor=NW, image=image)
    # image = Image.open("pj13.jpg")
    # image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), resample=Image.LANCZOS)

    # photo = ImageTk.PhotoImage(image)

    # labelle = tk.Label(root, image=photo)
    # labelle.place(x=0, y=0, relwidth=1, relheight=1)
    #img
    imgroot=Image.open("pj9.jpg")
    photoroot=ImageTk.PhotoImage(imgroot,master=root)
    img_label2=Label(root,image=photoroot)
    img_label2.place(width=1366,height=768)

        


    #main windodw
    label=Label(root,text="WELCOME TO INDIAN BANK ATM",fg="Yellow",bg="dark blue",font="verdana 30 bold")
    label.place(x=350,y=110)

    #name  main window
    mainwindowlab=Label(root,text=" Name: ",fg="Yellow",bg="dark blue",font="verdana 25 bold")
    mainwindowlab.place(x=380,y=200)
    # name entry
    name=Entry(root,width=30)
    name.place(x=700,y=210)

    #email id
    mainwindowlab1=Label(root,text=" E-mail ID: ",fg="Yellow",bg="dark blue",font="verdana 25 bold")
    mainwindowlab1.place(x=380,y=250)
    #mail id entry
    mail=Entry(root,width=30)
    mail.place(x=700,y=260)

    #phone number
    mainwindowlab2=Label(root,text=" Phone Number: ",fg="Yellow",bg="dark blue",font="verdana 25 bold")
    mainwindowlab2.place(x=380,y=300)
    #phone number entry
    phoneno=Entry(root,width=30)
    phoneno.place(x=700,y=310)
    #account no place
    mainwindowlab33=Label(root,text=" Account no: ",fg="Yellow",bg="dark blue",font="verdana 25 bold")
    mainwindowlab33.place(x=380,y=350)
    #account entry
    accountno=Entry(root,width=30)
    accountno.place(x=700,y=360)
    #password
    mainwindowlab3=Label(root,text=" Password: ",fg="Yellow",bg="dark blue",font="verdana 25 bold")
    mainwindowlab3.place(x=380,y=400)
    #password entry
    pwd=Entry(root,width=30)
    pwd.place(x=700,y=415)
    #button
    b=Button(root,text="CANCEL",width=15,fg="yellow",bg="dark blue",activebackground="light blue",font="verdana 19 bold")
    b.place(x=440,y=450)
    bb1=Button(root,text="SIGN UP",width=15,fg="yellow",bg="dark blue",activebackground="light blue",font="verdana 19 bold",command=fun)
    bb1.place(x=740,y=450)


#THANK YOU
def thank_you():
    global img9,photo9,w9
    w9=Tk()

    w9.title("ATM")
    w9.geometry("1366x768")
    #canvaas
    c = Canvas(w9, width=1366, height=768, bg='lawn green')
    c.grid(row=0, column=0)
    #img9
    img9=Image.open("pj11.jpg")
    photo9=ImageTk.PhotoImage(img9,master=w9)
    img_label2=Label(w9,image=photo9)
    img_label2.place(width=1366,height=768)
    
    # thank you come again
    lab10=Label(w9,text="THANK YOU",fg="Yellow",bg="dark blue",font="verdana 30 bold")
    lab10.place(x=520,y=250)
    # back to main page Button
    back_to_main_page=Button(w9,text="Back to home",bg="yellow",fg="dark blue",font="verdana 10 bold",command=fun)
    back_to_main_page.place(x=600,y=400)
    


#window_3  #deposit
def fun_2():
    global img4,photo4,e3,amount_deposited_succussfully
    w3=Tk()
    w3.title("Frame-4")
    w3.geometry("1366x768")
    
    #canvas
    d = Canvas(w3, width=1366, height=768, bg='lawn green')
    d.grid(row=0, column=0)
    #img
    #img
    img4=Image.open("pj.jpg")
    photo4=ImageTk.PhotoImage(img4,master=w3)
    img_label2=Label(w3,image=photo4)
    img_label2.place(width=1366,height=768)
    #label
    l4=Label(w3,text=" Deposit ",fg="Yellow",bg="dark blue",font="verdana 30 bold")
    l4.place(x=540,y=110)
    l5=Label(w3,text=" Enter Amount: ",fg="Yellow",bg="dark blue",font="verdana 25 bold")
    l5.place(x=380,y=200)
    e3=Entry(w3,width=30)
    e3.place(x=750,y=220)
    # amount dposited successfully
    # def amount_deposited_succussfully():
    #     amount_deposited_succussfullylab=Label(w3,text="Amount deposited successfully!",width=30,fg="yellow",bg="dark blue",font="verdana 30 bold")
    #     amount_deposited_succussfullylab.place(x=290,y=400)
    #     thank_you()
        # z=time.sleep(2)
        # print(z)
        # zz=root
        # print(zz)
    #cancel
    b5=Button(w3,text="cancel",width=13,fg="yellow",bg="dark blue",font="verdana 16 bold",command=fun_1)
    b5.place(x=490,y=300)
    # #message
    
    #ok
    b66=Button(w3,text="ok",width=13,fg="yellow",bg="dark blue",font="verdana 16 bold",command=add) #and clicked and amount_deposited_succussfully) #and w3.destroy)
    b66.place(x=720,y=300)
    #amount depostited suceesfully

    
    #message box
    
#window_4   #withdraw
def fun_3():
    global img3,e4,photo3
    w4=Tk()
    w4.title("Frame-4")
    w4.geometry("1366x768")
    
    #canvas
    f = Canvas(w4, width=1366, height=768, bg='lawn green')
    f.grid(row=0, column=0)
    # img3
    img3=Image.open("pj6.jpg")
    photo3=ImageTk.PhotoImage(img3,master=w4)
    img_label2=Label(w4,image=photo3)
    img_label2.place(width=1366,height=768)
    #label
    l6=Label(w4,text=" Withdraw ",fg="Yellow",bg="dark blue",font="verdana 30 bold")
    l6.place(x=540,y=110)
    l7=Label(w4,text=" Enter Amount: ",fg="Yellow",bg="dark blue",font="verdana 25 bold")
    l7.place(x=380,y=200)
    e4=Entry(w4,width=30)
    e4.place(x=750,y=220)
    
    #cancel
    b7=Button(w4,text="cancel",width=13,fg="yellow",bg="dark blue",font="verdana 16 bold",command=fun_1)
    b7.place(x=490,y=300)
    #ok
    b8=Button(w4,text="ok",width=13,fg="yellow",bg="dark blue",font="verdana 16 bold",command=sub)
    b8.place(x=720,y=300)

#window_5 #check balance
def fun_4():
    global img5,photo5,bal
    w5=Tk()
    w5.title("Frame-5")
    w5.geometry("1366x768")
    #canvas
    g = Canvas(w5, width=1366, height=768, bg='lawn green')
    g.grid(row=0, column=0)
    #imaage
    #img
    img5=Image.open("pj13.jpg")
    photo5=ImageTk.PhotoImage(img5,master=w5)
    img_label2=Label(w5,image=photo5)
    img_label2.place(width=1366,height=768)
    # label
    check_bal_lab=Label(w5,text="Your accout balance is ",fg="Yellow",bg="dark blue",font="verdana 30 bold")
    check_bal_lab.place(x=400,y=110)
    #rs
    check_bal_lab2=Label(w5,text="RS",fg="Yellow",bg="dark blue",font="verdana 30 bold")
    check_bal_lab2.place(x=400,y=180)
    # bal label
    check_bal_lab1=Label(w5,text=str(bal)+" /- only",fg="Yellow",bg="dark blue",font="verdana 30 bold")
    check_bal_lab1.place(x=465,y=180)
    #check balance back to home 1
    # back to main page Button
    back_to_main_page1=Button(w5,text="Back to home",bg="yellow",fg="dark blue",font="verdana 10 bold",command=fun)
    back_to_main_page1.place(x=600,y=400)
    
    
#window_2
def fun_1():
    global img2,photo22
    w2=Tk()
    w2.title("Frame-3")
    w2.geometry("1366x768")
     #canvas
    h = Canvas(w2, width=1366, height=768, bg='lawn green')
    h.grid(row=0, column=0)
            #img2
    img2=Image.open("pj1.jpg")
    photo22=ImageTk.PhotoImage(img2,master=w2)
    img_label2=Label(w2,image=photo22)
    img_label2.place(width=1366,height=768)
            #canvas
    l3=Label(w2,text="Select your option",fg="Yellow",bg="dark blue",font="verdana 30 bold")
    l3.place(x=400,y=110)
    a1=accountno.get()
    p1=pwd.get()
    print(a1,p1)
    cur.execute("select * from customer_into")
    for i in cur:
        if i[3]==a1 and i[4 ]==p1:
            
            
            
            #deposit
            b3=Button(w2,text="Deposit",width=13,fg="yellow",bg="dark blue",font="verdana 16 bold",command=fun_2)
            b3.place(x=490,y=300)

            #Withdraw
            b4=Button(w2,text="Withdraw",width=13,fg="yellow",bg="dark blue",font="verdana 16 bold",command=fun_3)
            b4.place(x=490,y=400)
            
            #Check balance
            b5=Button(w2,text="Check balance",width=13,fg="yellow",bg="dark blue",font="verdana 16 bold",command=fun_4)
            b5.place(x=490,y=500)


#window_1
def fun():
    global pwd,paas
    n=name.get()
    ml=mail.get()
    ph=phoneno.get()
    acc=accountno.get()
    paas=pwd.get()
    print(n,ml,ph,paas)
    query="insert into customer_into values(%s,%s,%s,%s,%s)"
    
    val=[n,ml,ph,acc,paas]
    print("Started")
    cur.execute(query,val)
    db.commit()
    print("Done")
    global img1,photo2
    w1=Tk()
    w1.title("Frame-2")
    w1.geometry("1366x768")
    
    # # #IMG
    # # img = PhotoImage(file="pj2.jpg")
    # # label = Label(w1,image=img)
    # # label.place(x=0, y=0)
    # # #canvas
    i = Canvas(w1, width=1366, height=768, bg='lawn green')
    i.grid(row=0, column=0)
    
    # canvas.create_image(0, 0, image=bg, anchor="nw")
    # Add the image file
    # bg = ImageTk.PhotoImage(file="pj3.jpg")

    # # Create a canvas
    # canvas = Canvas(w1,width= 400, height= 300)
    # canvas.pack(fill= "both", expand=True)

    # # Display image
    # canvas.create_image(0, 0, image=bg, anchor="nw")
    #img
    img1=Image.open("pj2.jpg")
    photo2=ImageTk.PhotoImage(img1,master=w1)
    img_label2=Label(w1,image=photo2)
    img_label2.place(width=1366,height=768)
    
    #label account
    l1=Label(w1,text="Account number : ",fg="Yellow",bg="dark blue",font="verdana 30 bold")
    l1.place(x=300,y=110)
    e=Entry(w1,width=30,)
    e.place(x=760,y=120)   
    l2=Label(w1,text="PIN:",fg="Yellow",bg="dark blue",font="verdana 30 bold")
    l2.place(x=500,y=180)
    e2=Entry(w1,width=30)
    e2.place(x=700,y=200)
    #login
    b1=Button(w1,text="login",width=13,fg="yellow",bg="dark blue",font="verdana 16 bold",command=fun_1)
    b1.place(x=490,y=300)
    #cancel
    b2=Button(w1,text="cancel",width=13,fg="yellow",bg="dark blue",font="verdana 16 bold",command=root)
    b2.place(x=720,y=300)
    #forgot pin
    l2=Label(w1,text="Forgot PIN?  ",fg="Yellow",bg="dark blue",font="verdana 17 bold")
    l2.place(x=800,y=400)

# label.pack()
#main page
bbwel=Button(welcome,text="CONTINUE",width=15,fg="yellow",bg="dark blue",activebackground="light blue",font="verdana 19 bold",command=root)
bbwel.place(x=540,y=450)


welcome.mainloop()