from tkinter import *
root=Tk()
#window size define by geometry
root.geometry("325x355+500+200")
#set title of calculator
root.title("Simple Calculator")
#root.resizable(False,False)
#define function for number ,clear and equal
def btnclick(number):
    global val
    val=val+str(number)
    data.set(val)
def btnclear():
        global val
        val=""
        data.set("")
def btnequal():
        global val
        result=str(eval(val))
        data.set(result)

val=""
data=StringVar()

#make entry box for calcultor
Entry(root,textvariable=data,width=18,bd=29,justify="right",bg="blue",font=("arial",20)).grid(row=0,column=1)
#define button of calcultor
button1=Button(root,text="AC",width=6,height=2,font="arial 12 bold",bd=1,fg="black",bg="red",command=btnclear).place(x=5,y=100)
button1=Button(root,text="x",width=6,height=2,font="arial 12 bold",bd=1,fg="black",bg="red",command=lambda:btnclick(x)).place(x=80,y=100)
button1=Button(root,text="+/_",width=6,height=2,font="arial 12 bold",bd=1,fg="black",bg="red",command=lambda:btnclick("+/_")).place(x=160,y=100)
button1=Button(root,text="/",width=6,height=2,font="arial 12 bold",bd=1,fg="black",bg="red",command=lambda:btnclick("/")).place(x=240,y=100)
button1=Button(root,text="7",width=6,height=2,font="arial 12 bold",bd=1,fg="black",bg="red",command=lambda:btnclick(7)).place(x=5,y=150)
button1=Button(root,text="8",width=6,height=2,font="arial 12 bold",bd=1,fg="black",bg="red",command=lambda:btnclick(8)).place(x=80,y=150)
button1=Button(root,text="9",width=6,height=2,font="arial 12 bold",bd=1,fg="black",bg="red",command=lambda:btnclick(9)).place(x=160,y=150)
button1=Button(root,text="*",width=6,height=2,font="arial 12 bold",bd=1,fg="black",bg="red",command=lambda:btnclick("*")).place(x=240,y=150)
button1=Button(root,text="4",width=6,height=2,font="arial 12 bold",bd=1,fg="black",bg="red",command=lambda:btnclick(4)).place(x=5,y=200)
button1=Button(root,text="5",width=6,height=2,font="arial 12 bold",bd=1,fg="black",bg="red",command=lambda:btnclick(5)).place(x=80,y=200)
button1=Button(root,text="6",width=6,height=2,font="arial 12 bold",bd=1,fg="black",bg="red",command=lambda:btnclick(6)).place(x=160,y=200)
button1=Button(root,text="-",width=6,height=2,font="arial 12 bold",bd=1,fg="black",bg="red",command=lambda:btnclick("-")).place(x=240,y=200)
button1=Button(root,text="1",width=6,height=2,font="arial 12 bold",bd=1,fg="black",bg="red",command=lambda:btnclick(1)).place(x=5,y=250)
button1=Button(root,text="2",width=6,height=2,font="arial 12 bold",bd=1,fg="black",bg="red",command=lambda:btnclick(2)).place(x=80,y=250)
button1=Button(root,text="3",width=6,height=2,font="arial 12 bold",bd=1,fg="black",bg="red",command=lambda:btnclick(3)).place(x=160,y=250)
button1=Button(root,text="+",width=6,height=2,font="arial 12 bold",bd=1,fg="black",bg="red",command=lambda:btnclick("+")).place(x=240,y=250)
button1=Button(root,text="%",width=6,height=2,font="arial 12 bold",bd=1,fg="black",bg="red",command=lambda:btnclick("%")).place(x=5,y=300)
button1=Button(root,text=0,width=6,height=2,font="arial 12 bold",bd=1,fg="black",bg="red",command=lambda:btnclick(0)).place(x=80,y=300)
button1=Button(root,text=".",width=6,height=2,font="arial 12 bold",bd=1,fg="black",bg="red",command=lambda:btnclick(".")).place(x=160,y=300)
button1=Button(root,text="=",width=6,height=2,font="arial 12 bold",bd=1,fg="black",bg="red",command=btnequal).place(x=240,y=300)

root.mainloop()





