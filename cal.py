from tkinter import*

def click(event):
    global scvalue
#event.widegt will give no which will be clicked by user
    text=event.widget.cget("text")
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            value=eval(screen.get())
    
        
        scvalue.set(value)   
        screen.update()
            
    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

top=Tk()

top.geometry("500x500")
top.title("calculator by rishav")
scvalue=StringVar()
scvalue.set("")
screen=Entry(top,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,ipady=5,padx=5)
#making frame and pack 3 buttons
f1=Frame(top,bg="grey")
#button inside frame
b1=Button(f1,text="9",bg="red",padx=5,pady=5,font="lucida 20 bold")
b1.pack(side=LEFT,padx=5,pady=5)
b1.bind("<Button-1>",click)

b2=Button(f1,text="8",bg="red",padx=5,pady=5,font="lucida 20 bold")
b2.pack(side=LEFT,padx=5,pady=5)
b2.bind("<Button-1>",click)

b3=Button(f1,text="7",bg="red",padx=5,pady=5,font="lucida 20 bold")
b3.pack(side=LEFT,padx=5,pady=5)
b3.bind("<Button-1>",click)

f1.pack()


f1=Frame(top,bg="grey")
#button inside frame
b4=Button(f1,text="6",bg="yellow",padx=5,pady=5,font="lucida 20 bold")
b4.pack(side=LEFT,padx=5,pady=5)
b4.bind("<Button-1>",click)

b5=Button(f1,text="5",bg="yellow",padx=5,pady=5,font="lucida 20 bold")
b5.pack(side=LEFT,padx=5,pady=5)
b5.bind("<Button-1>",click)

b6=Button(f1,text="4",bg="yellow",padx=5,pady=5,font="lucida 20 bold")
b6.pack(side=LEFT,padx=5,pady=5)
b6.bind("<Button-1>",click)

f1.pack()

f1=Frame(top,bg="grey")
#button inside frame
b7=Button(f1,text="3",bg="pink",padx=5,pady=5,font="lucida 20 bold")
b7.pack(side=LEFT,padx=5,pady=5)
b7.bind("<Button-1>",click)

b8=Button(f1,text="2",bg="pink",padx=5,pady=5,font="lucida 20 bold")
b8.pack(side=LEFT,padx=5,pady=5)
b8.bind("<Button-1>",click)

b9=Button(f1,text="1",bg="pink",padx=5,pady=5,font="lucida 20 bold")
b9.pack(side=LEFT,padx=5,pady=5)
b9.bind("<Button-1>",click)

f1.pack()

f1=Frame(top,bg="grey")
#button inside frame
b10=Button(f1,text="0",bg="green",padx=5,pady=5,font="lucida 20 bold")
b10.pack(side=LEFT,padx=5,pady=5)
b10.bind("<Button-1>",click)

b11=Button(f1,text=".",bg="green",padx=5,pady=5,font="lucida 20 bold")
b11.pack(side=LEFT,padx=5,pady=5)
b11.bind("<Button-1>",click)

b12=Button(f1,text="C",bg="green",padx=5,pady=5,font="lucida 20 bold")
b12.pack(side=LEFT,padx=5,pady=5)
b12.bind("<Button-1>",click)

f1.pack()

f1=Frame(top,bg="grey")
#button inside frame
b13=Button(f1,text="+",bg="purple",padx=5,pady=5,font="lucida 20 bold")
b13.pack(side=LEFT,padx=5,pady=5)
b13.bind("<Button-1>",click)

b14=Button(f1,text="-",bg="purple",padx=5,pady=5,font="lucida 20 bold")
b14.pack(side=LEFT,padx=5,pady=5)
b14.bind("<Button-1>",click)

b15=Button(f1,text="*",bg="purple",padx=5,pady=5,font="lucida 20 bold")
b15.pack(side=LEFT,padx=5,pady=5)
b15.bind("<Button-1>",click)

f1.pack()

f1=Frame(top,bg="grey")
#button inside frame
b16=Button(f1,text="/",padx=5,pady=5,font="lucida 20 bold")
b16.pack(side=LEFT,padx=5,pady=5)
b16.bind("<Button-1>",click)

b17=Button(f1,text="%",padx=5,pady=5,font="lucida 20 bold")
b17.pack(side=LEFT,padx=5,pady=5)
b17.bind("<Button-1>",click)

b18=Button(f1,text="=",padx=5,pady=5,font="lucida 20 bold")
b18.pack(side=LEFT,padx=5,pady=5)
b18.bind("<Button-1>",click)

f1.pack()


top.mainloop()





