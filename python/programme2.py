def addition():
   resultat =(2*2)
   return resultat
print("le resultat fait: ",addition())

age = int(input("ecriez votre age: "))
print(age)
passWord = input("ecrivez le mot de passe: ")
password_length = len(passWord)
if password_length<=8:
   print("c'est pas correcte")
else :
   print("c'est correcte")

liste = [1,2,3,'moi','ha','ha']
print(liste)
liste.extend=("moi","pas")
liste[0]=2

text = input("donner votre nom-penom").split("-")
print(text)
print("votre nom {}, votre prenom {}".format(text[0],text[1]))