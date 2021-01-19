from tkinter import *
from random import randrange
from random import choice

# Creation dune fenetre d'acueille 
fenetre=Tk()
fenetre.geometry("1350x680")
fenetre.minsize(1350,680)
fenetre.config(background='#F1C40F')
fenetre.title("ZCASINO")
# Creation de la fenetre pour le game 
def jouer() :
    fenetre.destroy()
    ouvrir=Toplevel(fenetre1)
fenetre1= Tk()
fenetre1.geometry("1350x680")
fenetre1.minsize(1350,680)
fenetre1.config(background="#F1C40F")
# Creation de Frame
frame = Frame(fenetre1, bg='#F1C40F', bd=2, relief=SUNKEN)
frame2 = Frame(fenetre1, bg='#F1C40F')
frame3 = Frame(fenetre1, bg='#F1C40F')
frame4 = Frame(fenetre1, bg='#F1C40F')
frame5 = Frame(fenetre1, bg='#F1C40F')
IA1= randrange(0,50)
IA2= randrange(0,50)
IA3= randrange(0,50)
money_IA1 = randrange(1, 3000)
money_IA2 = randrange(1, 3000)
money_IA3 = randrange(1, 3000)
#La methode integer
global var_texte
global chi_texte
# l'argent des joueurs 
money1 = 3000
money2 = 3000
money3 = 3000
money4 = 3000
# Quand les joueurs auront parié 
result_money1 = (money2-money_IA1)
result_money2 = (money3-money_IA2)
result_money3 = (money4-money_IA3)
# les tailles des images
height= 40
width= 40
height1= 92
width1= 92
#les fonctions pour les boutons
def mise():
    global var_texte
    var_texte = var_texte.get()
    var_texte = float(var_texte)
    global money_IA1
    global money_IA2
    global money_IA3
    global result_money1
    global result_money2
    global result_money3
    global result_money4
    money_player.config(text=result_money4)
    money_player2.config(text=result_money1)
    money_player3.config(text=result_money2)
    money_player4.config(text=result_money3)
    player_mise2.config(text=money_IA1)
    player_mise3.config(text=money_IA2)
    player_mise4.config(text=money_IA3)
    label_choix.config(text="appuyer sur Tirer")
def roulette():
    global ordi_choix
    label_choix.config(text=ordi_choix)
    if chi_texte == ordi_choix:
        tout = (money1+result_money4+money_IA1+money_IA2+money_IA3)
        money_player.config(text=tout)
        ordi_commente.config(text="WAW Bien Jouer")
    elif IA1 == ordi_choix :
        tout1 = (money1+result_money4+money_IA1+money_IA2+money_IA3)
        money_player2.config(text=tout1)
        ordi_commente.config(text="Loser")
    elif  IA2==ordi_choix:
        tout2 = (money1+result_money4+money_IA1+money_IA2+money_IA3)
        money_player3.config(text=tout2)
        ordi_commente.config(text="Loser")
    elif IA3== ordi_choix:
        tout3 = (money1+result_money4+money_IA1+money_IA2+money_IA3)
        money_player4.config(text=tout3)
        ordi_commente.config(text="Loser")
    else :
        ordi_commente.config(text="Loser")
def chiffre():
    global chi_texte
    chi_texte= chi_texte.get()
    chi_texte = float(chi_texte)
    global IA1
    global IA2
    global IA3
    player_choix.config(text=chi_texte)
    player_choix2.config(text=IA1)
    player_choix3.config(text=IA2)
    player_choix4.config(text=IA3)
# le corps du programme

#les label pour la roulette et les choix des chiffes de la roulette 
label_mise = Label(frame,  text=("La roulette:"),
                       font=("Tahoma", 26), bg='#F1C40F', fg='black')
label_choix = Label(frame, text="APPUYER SUR MISER",
                    font=("Tahoma", 26), bg='#2E4053', fg='white')

label_ordi = Label(frame,  text=("Commentaire:"),
                   font=("Tahoma", 26), bg='#F1C40F', fg='black')
ordi_commente = Label(frame, text=("Bonne Chance"),
                    font=("Tahoma", 26), bg='#F1C40F', fg='white')
# les label pour le joueurs 
image_player = PhotoImage(file="user_new1.png")
canvas_player = Canvas(frame2, height=height1, width=width1,
                        bg='#F1C40F', bd=0,  highlightthickness=0)
canvas_player.create_image(height/2, width/2, image=image_player)
mise_label1= Label(frame2,  text=("Votre Mise:"), 
                   font=("Tahoma", 14), bg='#F1C40F', fg='white')
var_texte= StringVar()
player_mise=Entry(frame2, textvariable= var_texte, font=("Tahoma", 16), bg='#2E4053', fg='white')

choix_label1 = Label(frame2,  text=("Votre Chiffre:"),
                     font=("Tahoma", 14), bg='#F1C40F', fg='white')
money_player = Label(frame2,  text=(money1, "$"),
                     font=("Tahoma", 14), bg='white', fg='black')
chi_texte= StringVar()
player_choix=Entry(frame2, textvariable=chi_texte, font=("Tahoma", 16), bg='#2E4053', fg='white')
#les label pour les bots, du bot1, 2 et 3
image2 = PhotoImage(file="gaming2.png")
canvas2 = Canvas(frame2, height=height, width=width,
                bg='#F1C40F', bd=0, highlightthickness=0)
canvas2.create_image(height/2, width/2, image=image2)
image_profil= PhotoImage(file="electronics_new4.png")
canvas_profil = Canvas(frame3, height=height1, width=width1,
                       bg='#F1C40F', bd=0,  highlightthickness=0)
canvas_profil.create_image(height1/2, width1/2, image=image_profil)
mise_label2 = Label(frame3,  text=("La mise:"),
                    font=("Tahoma", 14), bg='#F1C40F', fg='white')
player_mise2 = Label(frame3, text="0 $", font=(
        "Tahoma", 16), bg='#2E4053', fg='white')
choix_label2 = Label(frame3,  text=("Chiffre:"),
                     font=("Tahoma", 14), bg='#F1C40F', fg='white')
player_choix2 = Label(frame3, text=("_"), font=(
       "Tahoma", 16), bg='#2E4053', fg='white')
money_player2 = Label(frame3,  text=(money2,"$"),
                      font=("Tahoma", 14), bg='white', fg='black')
image3= PhotoImage(file="gaming2.png")
canvas3 = Canvas(frame3, height=height, width=width, bg='#F1C40F', bd=0, highlightthickness=0 )
canvas3.create_image(height/2, width/2, image=image3)
image_profil1 = PhotoImage(file="electronics_new4.png")
canvas_profil1 = Canvas(frame4, height=height1, width=width1,
                       bg='#F1C40F', bd=0,  highlightthickness=0)
canvas_profil1.create_image(height1/2, width1/2, image=image_profil1)
mise_label3 = Label(frame4,  text=("La Mise:"),
                    font=("Tahoma", 14), bg='#F1C40F', fg='white')
player_mise3 = Label(frame4, text="0 $", font=("Tahoma", 16), bg='#2E4053', fg='white')
choix_label3= Label(frame4,  text=("Chiffre:"), 
                    font=("Tahoma", 14), bg='#F1C40F', fg='white')
player_choix3 = Label(frame4, text=("_"), font=(
        "Tahoma", 16), bg='#2E4053', fg='white')
money_player3 = Label(frame4,  text=(money3, "$"),
                      font=("Tahoma", 14), bg='white', fg='black')
image4 = PhotoImage(file="gaming2.png")
canvas4 = Canvas(frame4, height=height, width=width,
                bg='#F1C40F', bd=0, highlightthickness=0)
canvas4.create_image(height/2, width/2, image=image2)
image_profil2 = PhotoImage(file="electronics_new4.png")
canvas_profil2 = Canvas(frame5, height=height1, width=width1,
                       bg='#F1C40F', bd=0,  highlightthickness=0)
canvas_profil2.create_image(height1/2, width1/2, image=image_profil2)
mise_label4 = Label(frame5,  text=("La Mise:"),
                       font=("Tahoma", 14), bg='#F1C40F', fg='white')
player_mise4 = Label(frame5, text="0 $", font=("Tahoma", 16), bg='#2E4053', fg='white')
choix_label4 = Label(frame5,  text=("Chiffre:"),
                     font=("Tahoma", 14), bg='#F1C40F', fg='white')
player_choix4 = Label(frame5, text=("_"), font=(
         "Tahoma", 16), bg='#2E4053', fg='white')
image = PhotoImage(file="gaming2.png")
canvas5 = Canvas(frame5, height=height, width=width, bg='#F1C40F', bd=0, highlightthickness=0)
canvas5.create_image(height/2, width/2, image=image)
money_player4 = Label(frame5,  text=(money4,"$"),
                      font=("Tahoma", 14), bg='white', fg='black ')
bouton_suivant = Button(frame2,  text=("  Miser  "),
                        font=("Tahoma", 14), bg='#2874A6', fg='white', command=mise)
bouton_jouer = Button(frame2,  text=("   Tirer   "),
                       font=("Tahoma", 14), bg='#2874A6', fg='white', command=roulette)
# La variable : ordi_choix 
ordi_choix = randrange(player_mise, IA1, IA2, IA3)
result_money4 = (money1-money_player)

#le positionnement de tous les elements du programme
canvas_profil1.grid(row=0, column=0, sticky=W)
mise_label3.grid(row=1, column=0,stick=W)
player_mise3.grid(row=2, column=0, stick=W)
choix_label3.grid(row=3, column=0, stick=W)
player_choix3.grid(row=4, column=0, stick=W)
canvas4.grid(row=2, column=1, sticky=W)
money_player3.grid(row=2, column=2, stick=W)
frame4.pack(side=TOP)
canvas_profil2.grid(row=0, column=0, sticky=W)
mise_label4.grid(row=1, column=0, stick=W)
player_mise4.grid(row=2, column=0, stick=W)
choix_label4.grid(row=3, column=0, stick=W)
player_choix4.grid(row=4, column=0, stick=W)
canvas5.grid(row=2, column=1, sticky=W)
money_player4.grid(row=2, column=2, stick=E)
frame5.pack(side=RIGHT)
canvas_profil.grid(row=0,column=0, sticky=W)
mise_label2.grid(row=1, column=0, stick=W)
player_mise2.grid(row=2, column=0, stick=W)
choix_label2.grid(row=3, column=0, stick=W)
player_choix2.grid(row=4, column=0, stick=W)
canvas3.grid(row=2, column=1, sticky=W)
money_player2.grid(row=2, column=2, stick=E)
frame3.pack(side=LEFT)
label_mise.pack()
label_choix.pack()
label_ordi.pack()
ordi_commente.pack()
frame.pack(expand=YES)
bouton_jouer.grid(row=3, column=4)
canvas_player.grid(row=0, column=1, sticky=W)
mise_label1.grid(row=1, column=1, stick=W)
player_mise.grid(row=2, column=1, stick=W)
choix_label1.grid(row=3, column=1, stick=W)
player_choix.grid(row=4, column=1, stick=W)
canvas2.grid(row=2, column=2, sticky=W)
money_player.grid(row=2, column=3, stick=W)
bouton_suivant.grid(row=1,column=4)
frame2.pack(side= BOTTOM)
#l'affichage de la fenetre1 
fenetre1.mainloop()
#les frames :
frame_fen= Frame(fenetre, bg='#F1C40F' )
frame_fen.pack(expand=YES)
frame_sign = Frame(fenetre, bg='#F1C40F')
frame_sign.pack(side=BOTTOM)
# Creation d'image pour l'acueille 
height2 = 350
width2 = 350
logo_game= PhotoImage(file="icone2.png")
canvas_logo= Canvas(frame_fen, width=width2, height=height2,
            bg= "#F1C40F" , bd=0, highlightthickness=0)
canvas_logo.create_image(height2/2, width2/2, image=logo_game)
canvas_logo.grid(row=0,column=0)
# Creation de bouton pour l'acueille 
button_jouer= Button(frame_fen, text="JOUER", font=("Tahoma",26)
            , bg='#2874A6', fg='white', command='jouer' )
button_jouer.grid(row=1,column=0)            
#signature 

fenetre.mainloop()
