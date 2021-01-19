from tkinter import *
fenetre = Tk()
fenetre.geometry("1000x849")
width=300
height=300
image = PhotoImage(file="roulette.jpg")
canvas = Canvas(width=width, height=height)
canvas.create_image(width/2, height/2, Iamge=image)
canvas.pack()
fenetre.mainloop()