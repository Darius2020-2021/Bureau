import os
from random import randrange
suite = False
choix = input("Veillez choisir un chiffre entre 0 et 49: ")
choix = int(choix)
if choix > 49 :
	print("il est plus superieur qu'a 49 on reprend")
	choix2 = input("Veillez choisir un chiffre entre 0 et 49: ")
	print("vous avez choisit le chiffre ", choix2)
	print("vous avez choisit le chiffre ", choix2)
    money2 = input("Combien d'argent misez vous?")
    print("vous avez miser ", money2, "$")
    roulette2 = randrange(0, 49)
    print("la roulette a choisit: ", roulette)
    if choix2 == roulette :
	   gagnant2 = (money*3)
	   print("vous avez gagné et vous avez obtenu ", gagnant2, "$")
    elif choix2 % 2 == 0 or choix2 % 4 == 0 or choix2 % 6 == 0 or choix2 % 8 == 0 or choix2 % 10 == 0:
	   moitié = (money//2)
	   print("vous avez presque ganger et vous avez obtenu ", moitié, "$")
	else:
		print("vous avez perdu et vous avez 0$")
print("vous avez choisit le chiffre ",choix)
money = input(" Combien d'argent misez vous? ")
money = int(money)
print("vous avez miser ",money,"$")
roulette = randrange(0,49)
print("la roulette a choisit: ",roulette)
if choix==roulette or choix2==roulette:
	gagnant =(money*3)
	print("vous avez gagné et vous avez obtenu ",gagnant,"$")
elif choix%2==0 or choix%4==0 or choix%6==0 or choix%8==0 or choix%10==0:
	moitié=(money//2)
	print("vous avez presque ganger et vous avez obtenu ",moitié,"$")
elif choix2 % 2 == 0 or choix2 % 4 == 0 or choix2 % 6 == 0 or choix2 % 8 == 0 or choix2 % 10 == 0:
	moitié = (money//2)
	print("vous avez presque ganger et vous avez obtenu ", moitié, "$")
else:
	print("vous avez perdu et vous avez 0$")

   
os.system("pause")
