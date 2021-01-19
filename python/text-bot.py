import os
savoir=["qu'est ce que tu sais faire ", "tu peux faire quoi", "que sais tu faire", "de quoi est ce que tu es capable"]
bot_name="Marx"
userName =input("Bonjour moi c'est "+bot_name+" et vous c'est quoi votre nom ?")
print("et bah ravi de vous rencontrer monsieur "+userName)
boulot= input("que puis je  faire pour vous ?")
if boulot == "qu'est ce que tu sais faire":
    print("je suis capable de plein de chose comme: devenir votre ami intime; vous aidez a travaillez; faire des recherhes internet a votre place; jouez aux jeux videos ou de la musique; vous donnez des conseils et pleins d,autre chose encore")
elif  boulot == "tu peux faire quoi":
    print("je suis capable de plein de chose comme: devenir votre ami intime; vous aidez a travaillez; faire des recherhes internet a votre place; jouez aux jeux videos ou de la musique; vous donnez des conseils et pleins d,autre chose encore")

os.system("pause")
