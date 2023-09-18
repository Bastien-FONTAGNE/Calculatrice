#Fonctions qui permet de faire une addition
def addition(a, b):
    return a + b
#Fonctions qui permet de faire une soustraction
def soustraction(a, b):
    return a - b
#Fonctions qui permet de faire une multiplication
def multiplication(a, b):
    return a * b
#Fonctions qui permet de faire une division
def division(a, b):
    if b == 0:
        return "Il est impossible de diviser par 0. Veuillez réessayer"
    else:
        return a / b
    
while True:

    #Menu de la calculatrice
    print("Menu de la calculatrice veuillez choisir votre option")
    print("Entrez 'addition' pour additioner des chiffres ou nombres (exemple 1+1 = 2)")
    print("Entrez 'soustraction' pour soustraire des chiffres ou nombres (exemple 1-1 = 0)")
    print("Entrer 'multiplication' pour multiplier des chiffres ou des nombres (exemple 2*2 = 4)")
    print("Entrer 'division' pour diviser des chiffres ou des nombres (exemple 2/2 = 1)")
    print("Entrer 'end' pour quitter la calculatrice") 

    choix = input(": ")
    #Quitte la calculatrice
    if choix == "end":
        break
        
    if choix in  ("additions, soustractions, multiplication, division"):
        num1 = float(input("Entrer le premier chiffre ou nombre: "))
        num2 = float(input("Entrer le deuxieme chiffre ou nombre: "))

    if choix == "addition":
        print("Resultat:", addition(num1, num2))
    elif choix == "soustraction":
        print("Resultat:", soustraction(num1, num2))
    elif choix == "multiplication":
        print("Resultat:", multiplication(num1, num2))
    elif choix == "division":
        print("Resultat", division(num1, num2))
    else:
        print("Options invalide veuillez réessayer")
