from tkinter import *
from tkinter.ttk import Treeview
import mysql.connector





win = Tk()
win.title("Marksheet")
win.geometry("854x480")


lab=Label(win,font=("Elephant", 50), text="MARKSHEET", fg='red').pack()




#SQL Conections...........


connect=mysql.connector.connect(host="localhost", user="root", passwd="8011", database="ncert")
cursor=connect.cursor()

sql= "SELECT * FROM MARKSHEET"
cursor.execute(sql)
rows= cursor.fetchall()
total= cursor.rowcount
print("Total Data Entries: "+str(total))








def btn1():             #Create/Edit
  prog1=Toplevel(win)
  prog1.title("Create/Edit")
  prog1.geometry("480x480")
  
  
  



  lab0=Label(prog1, text="Id",).pack()
  ent0=Entry(prog1)
  ent0.pack()

  lab1=Label(prog1, text="Name").pack()
  ent1=Entry(prog1)
  ent1.pack()

  lab2=Label(prog1, text="Class").pack()
  ent2=Entry(prog1)
  ent2.pack()
  
  lab3=Label(prog1, text="Roll no").pack()
  ent3=Entry(prog1)
  ent3.pack()
  
  lab4=Label(prog1, text="Marks").pack()
  ent4=Entry(prog1)
  ent4.pack()

  def savedata():
    id=ent0.get()
    Name=ent1.get()
    Class=ent2.get()
    Roll_no=ent3.get()
    Marks=ent4.get()
    cursor.execute("insert into marksheet(id, Name, Class, Roll_no, Marks) values('"+id+"','"+Name+"', '"+Class+"', '"+Roll_no+"', '"+Marks+"')")
    connect.commit()
    print("Record inserted!")



  btn=Button(prog1, text="Save Data", command=savedata).pack(pady=5)



  def editdata():
    id=ent0.get()
    Name=ent1.get()
    Class=ent2.get()
    Roll_no=ent3.get()
    Marks=ent4.get()
    cursor.execute("replace into marksheet(id, Name, Class, Roll_no, Marks) values('"+id+"','"+Name+"', '"+Class+"', '"+Roll_no+"', '"+Marks+"')")
    connect.commit()
    print("Record updated!")



  btn=Button(prog1, text="Update Data", command=editdata).pack(pady=5)







def btn2():             #Open list
  prog2=Toplevel(win)
  prog2.title("Open list")
  prog2.geometry("1050x480")
  prog2.resizable(0,0)

  frm=Frame(prog2)
  frm.pack(side=LEFT, padx=20)

  tv=Treeview(frm, columns=(1, 2, 3, 4,5), show="headings", height="20")
  tv.pack()

  tv.heading(1, text="ID")
  tv.heading(2, text="Name")
  tv.heading(3, text="Class")
  tv.heading(4, text="Roll No")
  tv.heading(5, text="Marks")

  for i in rows:
    tv.insert('','end', values=i)






def btn3():            #Open list By Roll No
  prog3=Toplevel(win)
  prog3.title("Open list By Roll No")
  prog3.geometry("854x480")

  ll=Label(prog3, text="Enter Roll no: ")
  ll.pack(pady=7)


  t1=Text(prog3, height=1, width=15)
  t1.pack(pady=7)

  my_str=StringVar()


  l2=Label(prog3, textvariable=my_str)
  l2.pack(pady=10)

  my_str.set("Output Here")

  b1=Button(prog3, text="Show Marksheet", command=lambda: my_details(t1.get('1.0',END)))
  b1.pack(pady=7)

  



  def my_details(id):
    try:
      val=int(id)
      
      try:
        cursor.execute("SELECT * FROM MARKSHEET WHERE Roll_no="+id)
        student=cursor.fetchone()
        my_str.set(student)
      except:
        my_str.set("Database Error")

    except:
      my_str.set("Check input")








def btn4():             #Delete
  prog4=Toplevel(win)
  prog4.title("About")
  prog4.geometry("854x480")


  lab0=Label(prog4, text="Id:",).pack()
  ent0=Entry(prog4)
  ent0.pack()

  def delete():
    id=ent0.get()
    cursor.execute("delete from marksheet where id=('"+id+"')")
    connect.commit()
    print("Record deleated!")

  btn=Button(prog4, text="Delete Data", command=delete).pack(pady=5)
  













button1 =  Button(win, text="Click Me To Create/Edit list",height=2,width=25,bg='yellow', command=btn1).pack()
button2 =  Button(win, text="Click Me To Open the list",height=2,width=25,bg='yellow', command=btn2).pack(pady=20)
button3 =  Button(win, text="Click Me To Search by Roll no",height=2,width=25,bg='yellow', command=btn3).pack()
button4 =  Button(win, text="Delete Data",height=2,width=10, bg='yellow', command=btn4).pack(anchor = "s", side = "right",padx=10, pady=10)



win.mainloop()
