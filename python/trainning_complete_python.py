import os

monaie= int(input("vous avez combien d'argent dans votre porte monaie ?"))
prix= 1000
    result=(monaie-prix)
    iphone= input("voudriez vous acheter un iphone à "+prix+ "$")
if iphone == oui :
    print("merci de votre achat il vous reste dans votre compte ", result)
elif iphone == non:
    print("Merci comme meme il vous reste ", monaie , "$")
else:
    print("Ok Merci")

os.system("pause")