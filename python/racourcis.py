import os 
import shutil
from tkinter import *
import webbrowser
def liengo():
   webbrowser.open_new("https://openclassrom.com")
def page():
    su= Toplevel(fenetre) 

def couper_fichier():
    cop = Toplevel(fenetre)
    cop.geometry("700x500")
    cop.config(background='#008080')
    file_expli = Label(cop, text="le nom du fichier",
                       font=("Tahoma", 13), bg='#008080', fg='white')
    file=Entry(cop, font=("Tahoma", 13), bg='white', fg='black' )
    target_expli = Label(cop, text="l'emplacement du fichier",
                       font=("Tahoma", 13), bg='#008080', fg='white')
    target = Entry(cop, font=("Tahoma", 13), bg='white', fg='black')
    new_bouton=Button(cop, text="couper",
    font=("Tahoma", 13), bg='white', fg='black', command=action_couper)
    file_expli.pack()
    file.pack()
    target_expli.pack()
    target.pack()
    new_bouton.pack()
def action_couper():
    pre_action = "target\file"
    shutil.copy(file, pre_action)
    os.remove(file)
def plus_info():
    i=Toplevel(fenetre)
    i.geometry("720x480")
     
fenetre = Tk()
fenetre.geometry("1080x620")
fenetre.minsize(480,360)
fenetre.title("Racourci")
fenetre.config(background="#008080")
frame = Frame(fenetre, bg='#008080')
introduction = Label(fenetre, text="veillez choisir un racourci", 
font=("Tahoma", 20), bg='#008080', fg='white')
intro_lien=Label(frame, text="lien de site:", 
font=("Tahoma",     17), bg='#008080', fg='white')
line0 = Button(frame, text="Openclassroom",
               font=("Tahoma", 13), bg='#a1e310', fg='white', command=liengo)
expli = Label(frame, text="couper, coller un fichier:",
              font=("Tahoma",    17), bg='#008080', fg='white')
choix = Entry(frame,font=("Tahoma", 17), bg='white', fg='black')
couper = Button(frame, text=("couper un fichier"),
                font=("Tahoma", 13),   bg='#a1e310', fg='white', command=couper_fichier)
fen = Button(frame, text="suite",
             font=("Tahoma", 13), bg='white', fg='black', command=page)
intro_lien.grid(row=0, column=0, stick=W)
introduction.pack()
line0.grid(row=1, column=0, stick=W)
frame.pack()
expli.grid(row=0, column=1, stick=E)
couper.grid(row=1, column=1, stick=E)
choix
menu=Menu(fenetre)
sous_menu = Menu(menu,  tearoff=0)
sous_menu.add_command(label="info", command=plus_info)
menu.add_cascade(label=Menu, menu=sous_menu)
fenetre.config(menu=menu)
fenetre.mainloop()
