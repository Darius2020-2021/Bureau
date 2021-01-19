from tkinter import *
fenetre= Tk()
fenetre.geometry("1080x720")
fenetre.minsize(720,480)
fenetre.title("moyenne_claculatrice")
fenetre.config(background='#729ab7')
height=110
width=150
frame= Frame(fenetre, bg='#729ab7')
frame2 = Frame(fenetre, bg='#729ab7')
image1= PhotoImage(file=("education.png")).zoom(35).subsample(32)
canvas= Canvas(frame, height=height, width=width, bg='#729ab7', bd=0, highlightthickness=0)
canvas.create_image(height/2, width/2, image=image1)
canvas.pack()
welcome = Label(frame, text="bienvenue à cal_moyenne",
font=("Tahoma, 20"), bg='#729ab7', fg='white')
welcome.pack()
frame.pack()
commence= Label(frame2, text="veillez ecrire vos moyenne de classe", 
                font=("Tahoma", 15), bg='#729ab7', fg='white')            
commence.pack()
moyen1 = Entry(frame2, font=("Tahoma", 15), bg='white', fg='black')moyen1.pack()
frame2.pack()
menu= Menu(fenetre)
menu.add_command(label="Quitter", command=fenetre.quit)
fenetre.config(menu=menu)
fenetre.mainloop()
