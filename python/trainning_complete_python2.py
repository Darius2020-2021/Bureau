import os
argent = int(input("vous avez combien d'argent ?"))
mineur= 7
majeur= 12
reste1 = (argent-mineur)
reste2 = (argent-majeur)
popcorn= 5
pop= (reste1-popcorn )
print("super vous avez "+argent+ " euro")
print("Les places de cinema varient selon l'âge")
age=int(input("1.Vous etes majeur et les places vous couterons 7 euro; 2.Vous etes mineur et les places vous couterons 12 euro" ))
if age == 1:
	print(" super bon film petit il te reste comme argent "+reste1+ " euro")
	achat= input("souhaitez vous acheter du popcorn ?")
    if achat== "oui":
	    print("merci pour votre achat il vous reste "+pop)
else:
	print(" super bon film monsieur il vous reste comme argent "+reste2+ " euro")
    achat= input("souhaitez vous acheter du popcorn ?")
	if achat== "non":
	    print("ok tant pis")
os.system(pause)