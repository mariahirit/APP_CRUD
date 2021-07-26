from tkinter import *
from tkinter import messagebox
import sqlite3


# ---------funcion----------------------------

def conexBBDD():

    miConex = sqlite3.connect("Users")

    miCursor = miConex.cursor()

    try:

        miCursor.execute('''
                     CREATE TABLE DATEUSERS(
                         ID INTEGER PRIMARY KEY AUTOINCREMENT,
                         NUME_USERS VARCHAR(50),
                         PRENUME VARCHAR(10),
                         PASSWORD VARCHAR(50),
                         ADRESA VARCHAR(50),
                         COMENTARIU VARCHAR(100))

                     ''')

        messagebox.showinfo("BBDD", "BBDD super")

    except:

        messagebox.showwarning("Atencion!", "Exista")


def salirApp():

    val = messagebox.askquestion("Salir", "Esti sigur ca vrei sa iesi!")
    if val == "yes":
        root.destroy()


def cleanField():
    miId.set("")
    miNume.set("")
    miPrenume.set("")
    miPass.set("")
    miAdresa.set("")
    textComentariu.delete(1.0, END)


def crear():
    miConex = sqlite3.connect("Users")

    miCursor = miConex.cursor()

    data = miNume.get(), miPrenume.get(), miPass.get(
    ), miAdresa.get(), textComentariu.get("1.0", END)
    """ miCursor.execute("INSERT INTO DATEUSERS VALUES(NULL, '" + miNume.get() +
                     "','" + miPass.get() +
                     "','" + miPrenume.get() +
                     "','" + miAdresa.get() +
                     "','" + textComentariu.get("1.0", END) + "') ") """

    miCursor.execute("INSERT INTO DATEUSERS VALUES(NULL, ?,?,?,?,? )", (data))
    miConex.commit()

    messagebox.showinfo("BBDD", "SUCCESFULY INSERT!")


def read():
    miConex = sqlite3.connect("Users")

    miCursor = miConex.cursor()

    miCursor.execute("SELECT * FROM DATEUSERS WHERE ID=" + miId.get())

    elUser = miCursor.fetchall()

    for user in elUser:
        miId.set(user[0])
        miNume.set(user[1])
        miPrenume.set(user[2])
        miPass.set(user[3])
        miAdresa.set(user[4])
        textComentariu.insert(1.0, user[5])

    miConex.commit()


def update():
    miConex = sqlite3.connect("Users")

    miCursor = miConex.cursor()

    miCursor.execute("UPDATE DATEUSERS  SET NUME_USERS ='" + miNume.get() +
                     "', PRENUME='" + miPrenume.get() +
                     "', PASSWORD='" + miPass.get() +
                     "', ADRESA='" + miAdresa.get() +
                     "', COMENTARIU='" + textComentariu.get("1.0", END) +
                     "' WHERE ID =" + miId.get()
                     )

    miConex.commit()

    messagebox.showinfo("BBDD", "SUCCESFULY UPDATE!")


def delete():

    miConex = sqlite3.connect("Users")

    miCursor = miConex.cursor()

    miCursor.execute("DELETE FROM DATEUSERS WHERE ID =" + miId.get())

    miConex.commit()

    messagebox.showinfo("BBDD", "SUCCESFULY DELETE!")


root = Tk()

navmenu = Menu(root)
root.config(menu=navmenu, width=300, height=300)

bbddMenu = Menu(navmenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexBBDD)
bbddMenu.add_command(label="Salir", command=salirApp)


deleteMenu = Menu(navmenu, tearoff=0)
deleteMenu.add_command(label="Delete field ", command=cleanField)

crudMenu = Menu(navmenu, tearoff=0)
crudMenu.add_command(label="Create ", command=crear)
crudMenu.add_command(label="Read ", command=read)
crudMenu.add_command(label="Update", command=update)
crudMenu.add_command(label="Delete", command=delete)

helpMenu = Menu(navmenu, tearoff=0)
helpMenu.add_command(label="License ")
helpMenu.add_command(label="About.... ")

navmenu.add_cascade(label="BBDD", menu=bbddMenu)
navmenu.add_cascade(label="DELETE", menu=deleteMenu)
navmenu.add_cascade(label="CRUD", menu=crudMenu)
navmenu.add_cascade(label="HELP", menu=helpMenu)


# --------------------  incep campurile -------------


miFrame = Frame(root)
miFrame.pack()

miId = StringVar()
miNume = StringVar()
miPrenume = StringVar()
miPass = StringVar()
miAdresa = StringVar()


packID = Entry(miFrame, textvariable=miId)
packID.grid(row=0, column=1, padx=10, pady=10)

packNume = Entry(miFrame, textvariable=miNume)
packNume.grid(row=1, column=1, padx=10, pady=10)
packNume.config(fg="red", justify="right")

packPrenume = Entry(miFrame, textvariable=miPrenume)
packPrenume.grid(row=2, column=1, padx=10, pady=10)

packPass = Entry(miFrame, textvariable=miPass)
packPass.grid(row=3, column=1, padx=10, pady=10)
packPass.config(show="?")


packAdresa = Entry(miFrame, textvariable=miAdresa)
packAdresa.grid(row=4, column=1, padx=10, pady=10)


textComentariu = Text(miFrame, width=16, height=5)
textComentariu.grid(row=5, column=1, padx=10, pady=10)

scrollVert = Scrollbar(miFrame, command=textComentariu.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

textComentariu.config(yscrollcommand=scrollVert.set)


# ---------------------------label ------------------------

idLabel = Label(miFrame, text="Id:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

numeLabel = Label(miFrame, text="Nume:")
numeLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

prenumeLabel = Label(miFrame, text="Prenume:")
prenumeLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passLabel = Label(miFrame, text="Password:")
passLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

adresaLabel = Label(miFrame, text="Adresa:")
adresaLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

textComentariuLabel = Label(miFrame, text="Comentariu:")
textComentariuLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)


# ------------------------button----------------

miFrame2 = Frame(root)
miFrame2.pack()

buttonCrear = Button(miFrame2, text="Create", command=crear)
buttonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

buttonRead = Button(miFrame2, text="Read", command=read)
buttonRead.grid(row=1, column=1, sticky="e", padx=10, pady=10)

buttonUpdate = Button(miFrame2, text="Update", command=update)
buttonUpdate.grid(row=1, column=2, sticky="e", padx=10, pady=10)

buttonDelete = Button(miFrame2, text="Delete", command=delete)
buttonDelete.grid(row=1, column=3, sticky="e", padx=10, pady=10)


root.mainloop()
