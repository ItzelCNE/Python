import random as Rand


def GameLogic(Pchoice, Bchoice):

    print("Seleccionaste " + Pchoice)
    print("El bot selecciono " + Bchoice)

    if Pchoice == Bchoice:
        print("Empate!")
    #----------- Tijera -------------
    elif Pchoice == "Tijera":    
        if Bchoice == "Piedra": 
            print("Perdiste!")
        else: 
            print("Ganaste")
    #----------- Piedra -------------
    elif Pchoice == "Piedra":
        if BChoice == "Papel": 
            print("Perdiste!")
        else: 
            print("Ganaste!")
    #------------ Papel -------------
    elif Pchoice == "Papel":
        if Bchoice == "Tijera": 
            print("Perdiste!")
        else: 
            print("Ganaste!")
            
       
BChoice = None
PChoice = None
options = ["Tijera","Papel","Piedra"]
i = 1

while i == 1:

 # Definicion eleccion del bot
 BChoice = Rand.choice(options)
 
 # Definicion eleccion del jugador
 PChoice = input("Piedra, papel o tijera? ")
 PChoice.capitalize
 
 #Definicion ganador
 GameLogic(str(PChoice),BChoice)

 


