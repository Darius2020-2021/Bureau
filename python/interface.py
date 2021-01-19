from tkinter import *
import webbrowser
def lien():
    webbrowser.open_new("http://microsoft.com")
fenetre = Tk()
fenetre.geometry('1080x480')
fenetre.title("PY")
fenetre.minsize(480,360)
fenetre.config(background='#677B8A')
frame = Frame(fenetre, bg='#677B8A')
labelText=Label(frame, text="bonjour tout le monde", font=("Tahoma", 30), bg='#677B8A',fg='white')
labelText.pack(expand=YES)
labelsubtext = Label(frame, text="bonjour tout le monde",
                  font=("Tahoma", 15), bg='#677B8A', fg='white')
labelsubtext.pack(expand=YES)
bouton = Button(frame, text="Ouvrir YT", font=(
    "Tahoma", 16), bg='white', fg='#677B8A', command=lien)
bouton.pack()
frame.pack(expand=YES)
fenetre.mainloop()
