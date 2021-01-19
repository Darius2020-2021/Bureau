class playeur:
    def __init__(self,pseudo,sante,attack):
       self.pseudo=pseudo
       self.sante= sante
       self.attack=attack
       print("votre nom est ",pseudo," votre sante est de ",sante," et votre attack est de ",attack)
       def get_pseudo(self):
           return self.pseudo
       def get_sante(self):
           return self.sante
       def get_attack(self):
           return self.attack
       def get_dommage(self, dommage):
            self.sante-= dommage
            print("vous venez de subir des degasts ",dommage)

player1= playeur("med",20,4)
player1.dommage(3)
print("Aie j'ai eu des degats il me reste ", player1.get_sante(), "vie")

player2 = playeur("mous",29,1)

