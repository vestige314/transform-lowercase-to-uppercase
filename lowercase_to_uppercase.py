def minVersMaj(chaineMin):
    
    chaineMaj = ""         #Initialise les variables
    nbChar = 0
    
    for lettre in chaineMin: 
        
        code = ord(lettre)
        code += -32               #fait une adition qui permet de passer le code ASCII des miniscule en majuscule
        chaineMaj += chr(code)    #crée la chaine de caractére en Majuscule
        nbChar += 1               #compte les caractére
        
    return chaineMaj, nbChar



chaineMin = input("Quelle est votre chaine de caractére")  #Demande à l'ultilisateur quelle est sa chaine de caractére en minuscule
while chaineMin != "" :
    minVersMaj(chaineMin)  #appele la fonction 
    print("La chaine de caractéres " + chaineMin + " transformée en majuscule devient " + minVersMaj(chaineMin)[0] + " et contient " + str(minVersMaj(chaineMin)[1]) + " caractères.")
    chaineMin = ""         #permet de finir la boucle while 