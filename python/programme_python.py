import os
annee = input("donne moi une année : ")
annee = int(annee)
continu = False
if annee%4==0:
   continu = True
   print("super tu as trouver")
elif annee%100==0:
   continu = False
   print("desolé mais c'est faux")
elif annee%400==0:
   continu=True
   print("c'est à peu prêt bon")
else:
   print("c'est totalement faux")
   try:
   	annee= int(annee)
   except:
    print("une erreur")

os.system("pause")