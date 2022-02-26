from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
from mysql import connector as sql
global i1
def passenger():
    gate = Tk()
    gate.title("Passengers")
    gate.geometry("1366x786")
    gate.config(bg="lightslategray")
    gate.iconbitmap("bil.ico")
    lbl = Label(gate,text="Alibaba Bus Passengers",font=("Arial 20 bold"),bg="orange",fg="black",relief="raised")
    lbl.pack(fill=X)
    col = ('id', 'name', 'age', 'gender', 'place')
    treeview = ttk.Treeview(gate, height=100, show="headings", columns=col)

    treeview.column('id', width=200, anchor=W)
    treeview.column('name', width=300, anchor=W)
    treeview.column('age', width=300, anchor=W)
    treeview.column('gender', width=300, anchor=W)
    treeview.column('place', width=300, anchor=W)

    treeview.heading('id', text="ID", anchor=W)
    treeview.heading('name', text="Name", anchor=W)
    treeview.heading('age', text="Age", anchor=W)
    treeview.heading('gender', text="Gender", anchor=W)
    treeview.heading('place', text="Place", anchor=W)

    treeview.place(x=0, y=40)

    dbs = sql.connect(host="localhost", user="root", passwd="root", database="passengers")
    cur = dbs.cursor()

    cur.execute("SELECT * FROM members")
    data = cur.fetchall()
    for i in data:
        treeview.insert(parent="",index="end",values=(i[0],i[1],i[2],i[3],i[4]))
    dbs.commit()
    gate.mainloop()

def op():
    boot = Tk()
    boot.title("Alibaba Tickets")
    boot.geometry("1366x786")
    boot.config(bg="lightslategray")
    boot.iconbitmap("bil.ico")

    def book():
        a = n1.get()
        b = a1.get()
        c = g1.get()
        d = p1.get()
        dbs = sql.connect(host="localhost",user="root",passwd="root",database="passengers")
        cur = dbs.cursor()
        val = (a,b,c,d,)
        s = "INSERT INTO members(id,name,age,gender,place) values(null,%s,%s,%s,%s)"
        cur.execute(s,val)
        dbs.commit()
        lastid = cur.lastrowid
        messagebox.showinfo("Your Booking is submitted", "Sucessfully")
        n1.delete(0,END)
        a1.delete(0, END)
        g1.delete(0, END)
        p1.delete(0, END)
        n1.focus_set()
    def delete():
        i = i1.get()
        dbs = sql.connect(host="localhost", user="root", passwd="root", database="passengers")
        cur = dbs.cursor()
        cur.execute("delete from members where id = %s",(i,))
        messagebox.showinfo("Your Booking is deleted", "Sucessfully")
        dbs.commit()
        n1.delete(0, END)
        a1.delete(0, END)
        g1.delete(0, END)
        p1.delete(0, END)
        i1.delete(0, END)
        n1.focus_set()


    def update():
        a = (n1.get())
        b = (a1.get())
        c = (g1.get())
        d = (p1.get())
        i = i1.get()
        dbs = sql.connect(host="localhost", user="root", passwd="root", database="passengers")
        cur = dbs.cursor()
        cur.execute("update members set name = %s, age = %s, gender = %s, place=%s where id= %s",(a,b,c,d,i,))
        messagebox.showinfo("Your Booking is updated", "Sucessfully")
        dbs.commit()
        n1.delete(0, END)
        a1.delete(0, END)
        g1.delete(0, END)
        p1.delete(0, END)
        i1.delete(0, END)
        n1.focus_set()

    #my_img = ImageTk.PhotoImage(file="bus.jpg")
    #label1 = Label(boot)
    #label1.place(x=10, y=100, width=200, height=250)
    #label1.config(image=my_img)

    head = LabelFrame(boot,text="Alibaba Ticket Booking",font=("Times 30 bold"),bg="lightslategray",fg="red")
    head.place(x = 500, y = 100)

    name = Label(head,text="Name",font=("Times 15 bold"),bg="lightslategray",fg="black")
    name.grid(row = 0,column = 0, padx = 10, pady = 10,sticky="w")

    age = Label(head, text="Age", font=("Times 15 bold"), bg="lightslategray", fg="black")
    age.grid(row=1, column=0, padx = 10, pady = 10,sticky="w")

    gender = Label(head, text="Gender", font=("Times 15 bold"), bg="lightslategray", fg="black")
    gender.grid(row=2, column=0, padx = 10, pady = 10,sticky="w")

    place = Label(head, text="Place", font=("Times 15 bold"), bg="lightslategray", fg="black")
    place.grid(row=3, column=0, padx = 10, pady = 10,sticky="w")

    id = name = Label(head, text="ID", font=("Times 15 bold"), bg="lightslategray", fg="black")
    name.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    n1 = Entry(head, font=("Times 15 bold"), bg="lightslategray", fg="black")
    n1.grid(row = 0, column = 1, padx = 10, pady = 10)

    a1 = Entry(head, font=("Times 15 bold"), bg="lightslategray", fg="black")
    a1.grid(row=1, column=1, padx = 10, pady = 10)

    g1 = Entry(head, font=("Times 15 bold"), bg="lightslategray", fg="black")
    g1.grid(row=2, column=1, padx = 10, pady = 10)

    p1 = Entry(head, font=("Times 15 bold"), bg="lightslategray", fg="black")
    p1.grid(row=3, column=1, padx = 10, pady = 10)

    i1 = Entry(head, font=("Times 15 bold"), bg="lightslategray", fg="black")
    i1.grid(row=4, column=1, padx=10, pady=10)


    btn2 = Button(head, text = "Book Now",font=("Times 10 bold"), bg="orange", fg="black",relief="raised",bd = "5",command=book)
    btn2.grid(row= 5, column=1, padx = 10, pady = 10,sticky="w")

    btn2 = Button(head, text="Passengers", font=("Times 10 bold"), bg="orange", fg="black", relief="raised", bd="5",
                  command=passenger)
    btn2.grid(row=5, column=2, padx=10, pady=10, sticky="w")

    btn3 = Button(head, text="Delete", font=("Times 10 bold"), bg="orange", fg="black", relief="raised", bd="5",
                  command=delete)
    btn3.grid(row=5, column=3, padx=10, pady=10, sticky="w")

    btn4 = Button(head, text="Update", font=("Times 10 bold"), bg="orange", fg="black", relief="raised", bd="5",
                  command=update)
    btn4.grid(row=5, column=4, padx=10, pady=10, sticky="w")
    boot.mainloop()




root = Tk()
root.title("Alibaba Tickets")
root.geometry("1366x786")
root.config(bg="lightslategray")
root.iconbitmap("tri.ico")

def close():
    a = messagebox.askyesno("Click Yes","Do You Really want to Exit?")
    if a == 1:
        quit()
    elif a == 0:
        return
lbl = Label(root,text="Welcome to Alibaba Ticket Booking",bg="orange",relief="raised",font=("Calibri 40 bold"),fg="gray")
lbl.pack(fill=X)


lbl = Label(root,text="We are help to booking easy at your time at your place.",bg="lightslategray",font=("Teletype 25 bold"),fg="red")
lbl.place(x = 100, y = 300)
btn = Button(root,text="Open",bg="green",relief="raised",font=("Calibri 20 bold"),fg="gray",bd="5",command=op)
btn.place(x = 550, y = 400)
btn1 = Button(root,text="Close",bg="red",relief="raised",font=("Calibri 20 bold"),fg="gray",bd="5",command=close)
btn1.place(x = 650, y = 400)

root.mainloop()