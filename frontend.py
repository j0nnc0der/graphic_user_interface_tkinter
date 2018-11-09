#Import everythihing from tkinter
from Tkinter import *

#Create window object
window=Tk()

#define four labels Title Author ISBN
li=Label(window, text="Title")
li.grid(row=0, column=0)

li=Label(window, text="Author")
li.grid(row=0, column=2)

li=Label(window, text="Year")
li.grid(row=1, column=0)

li=Label(window, text="ISBN")
li.grid(row=2, column=2)

#define Entries
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

#define ListBox
list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

#attatch scroll bar to the list
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1configure(yscrollcommand=sb1.set)
sbl.configure(command=list1.yview)

#Define buttons
b1=Button(window,text="View All", width=12)
b2.grid(row=2,column=3)

b1=Button(window,text="Search Entry", width=12)
b2.grid(row=3,column=3)

b1=Button(window,text="Add Entry", width=12)
b2.grid(row=4,column=3)

b1=Button(window,text="Updated selected", width=12)
b2.grid(row=5,column=3)

b1=Button(window,text="Delete selected", width=12)
b2.grid(row=6,column=3)

b1=Button(window,text="View All", width=12)
b2.grid(row=7,column=3)

b1=Button(window,text="View All", width=12)
b2.grid(row=8,column=3)


window.mainloop()


