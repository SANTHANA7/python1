from tkinter import*
import webbrowser
import cx_oracle
def santhana():
    name=text1.get()
    name1=text2.get()
    if name=="BANGTAN" and name1=="ARMY":
        print("welcome ARMY")
        webbrowser.open("http://www.google.co.in")
    else:
        print("invalid login")
a=Tk()
a.title("BTS")
a.geometry("300x300")
a.configure(background="purple")
Label(a,text="username",font=60,fg="white",bg="black").grid(row=1,column=1)
Label(a,text="password",font=60,fg="white",bg="black").grid(row=2,column=1)
text1=Entry(a,width=20,bg="white")
text1.grid(row=1,column=2)
text2=Entry(a,width=20,bg="white")
text2.grid(row=2,column=2)
e=Button(a,width=10,text="submit",bg="black",fg="white",font=20,command=santhana)
e.grid(row=5,column=2)
