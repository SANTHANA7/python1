Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import*
>>> a=TK()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a=TK()
NameError: name 'TK' is not defined
>>> from tkinter import*
>>> a=Tk()
>>> a.title("BTS")
''
>>> main.geometry("300x300")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    main.geometry("300x300")
NameError: name 'main' is not defined
>>> from tkinter import*
>>> a=Tk()
>>> a.title("BTS")
''
>>> a.geometry("300x300")
''
>>> a.configure(background='black')
>>> from tkinter import*
>>> a=Tk()
>>> a.title("BTS")
''
>>> a.geometry("300x300")
''
>>> 
>>>a.configure(background='purple')
>>> Label(a,text="BTS",font=60,fg="black",bg="white").grid(row=1,coloumn=1)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    Label(a,text="BTS",font=60,fg="black",bg="white").grid(row=1,coloumn=1)
  File "C:\Users\STC RS2 C3\AppData\Local\Programs\Python\Python37\lib\tkinter\__init__.py", line 2226, in grid_configure
    + self._options(cnf, kw))
_tkinter.TclError: bad option "-coloumn": must be -column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky
>>> Label(a,text="BTS",font=60,fg="black",bg="white").grid(row=1,column=1)
>>> Label(a,text="ARMY",font=60,fg="black",bg="white").grid(row=2,column=1)
>>> text1=Entry(main,width=20,bg="white")
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    text1=Entry(main,width=20,bg="white")
NameError: name 'main' is not defined
>>> 
>>> text1=Entry(a,width=20,bg="white")
>>> text1.grid(row=1,column=2)
>>> text2=Entry(a,width=20,bg="white")
>>> text2.grid(row=2,column=2)
>>> b=Button(a,width=10,text="submit",bg=white,fg="black",font=20)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    b=Button(a,width=10,text="submit",bg=white,fg="black",font=20)
NameError: name 'white' is not defined
>>> b=Button(a,width=10,text="submit",bg="white",fg="black",font=20)
>>> b.grid(row=5,column=2)
>>> b.grid(row=5,column=3)
>>> Label(a,text="BTS ",font=60,fg="black",bg="white").grid(row=1,column=1)
>>> Label(a,text=" BTS ",font=60,fg="black",bg="white").grid(row=1,column=1)
>>> Label(a,text="  BTS  ",font=60,fg="black",bg="white").grid(row=1,column=1)
>>> Label(a,text=" ARMY ",font=60,fg="black",bg="white").grid(row=2,column=1)
>>> Label(a,text=" ARMY",font=60,fg="black",bg="white").grid(row=2,column=1)
>>> Label(a,text="ARMY",font=60,fg="black",bg="white").grid(row=2,column=1)
>>>Label(a,text="   BTS   ",font=60,fg="black",bg="white").grid(row=1,column=1
                                                                
>>> 
