from tkinter import *

root=Tk()
mylabel=Label(root,text="Calculator")
mylabel.grid()

input_E1=Entry(root,width=25,borderwidth=5)
input_E1.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def get_number(number):
    input_E1.delete(0,END)
    current=input_E1.get()
    input_E1.delete(0,END)
    input_E1.insert(0,str(current)+str(number))
    
def add():
    first_num=input_E1.get()
    global f_num
    global math
    math="add"
    f_num=int(first_num)
    input_E1.delete(0,END)
    
def sub():
    first_num=input_E1.get()
    global f_num
    global math
    math="sub"
    f_num=int(first_num)
    input_E1.delete(0,END)
    
def mul():
    first_num=input_E1.get()
    global f_num
    global math
    math="mul"
    f_num=int(first_num)
    input_E1.delete(0,END)
    
def div():
    first_num=input_E1.get()
    global f_num
    global math
    math="div"
    f_num=int(first_num)
    input_E1.delete(0,END)
    
def equal():
    second_num=input_E1.get()
    input_E1.delete(0,END)
    if math=="add":
        input_E1.insert(0,f_num+int(second_num))
    if math=="sub":
        input_E1.insert(0,f_num-int(second_num))
    if math=="mul":
        input_E1.insert(0,f_num*int(second_num))
    if math=="div":
        input_E1.insert(0,f_num/int(second_num))
    
    
def clear():
    input_E1.delete(0,END)
    
    

mybutton_1=Button(root,text="1",pady=40,padx=40,command=lambda: get_number(1))
mybutton_2=Button(root,text="2",pady=40,padx=40,command=lambda: get_number(2))
mybutton_3=Button(root,text="3",pady=40,padx=40,command=lambda: get_number(3))
mybutton_4=Button(root,text="4",pady=40,padx=40,command=lambda: get_number(4))
mybutton_5=Button(root,text="5",pady=40,padx=40,command=lambda: get_number(5))
mybutton_6=Button(root,text="6",pady=40,padx=40,command=lambda: get_number(6))
mybutton_7=Button(root,text="7",pady=40,padx=40,command=lambda: get_number(7))
mybutton_8=Button(root,text="8",pady=40,padx=40,command=lambda: get_number(8))
mybutton_9=Button(root,text="9",pady=40,padx=40,command=lambda: get_number(9))
mybutton_0=Button(root,text="0",pady=40,padx=40,command=lambda: get_number(0))
mybutton_add=Button(root,text="+",pady=40,padx=40,command=add)
mybutton_sub=Button(root,text="-",pady=40,padx=40,command=sub)
mybutton_mul=Button(root,text="*",pady=40,padx=40,command=mul)
mybutton_div=Button(root,text="/",pady=40,padx=40,command=div)
mybutton_equal=Button(root,text="=",pady=40,padx=88,command=equal)
mybutton_clear=Button(root,text="clear",pady=40,padx=80,command=clear)

mybutton_7.grid(row=1,column=0)
mybutton_8.grid(row=1,column=1)
mybutton_9.grid(row=1,column=2)

mybutton_4.grid(row=2,column=0)
mybutton_5.grid(row=2,column=1)
mybutton_6.grid(row=2,column=2)

mybutton_1.grid(row=3,column=0)
mybutton_2.grid(row=3,column=1)
mybutton_3.grid(row=3,column=2)

mybutton_0.grid(row=4,column=0)
mybutton_clear.grid(row=4,column=1,columnspan=2)

mybutton_add.grid(row=5,column=0)
mybutton_equal.grid(row=5,column=1,columnspan=2)

mybutton_sub.grid(row=6,column=0)
mybutton_mul.grid(row=6,column=1)
mybutton_div.grid(row=6,column=2)

root.mainloop()