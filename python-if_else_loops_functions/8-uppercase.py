#!/usr/bin/python3

def uppercase(var):
	if 97 <= ord(var) <= 122:
        	resultat += chr(ord(var) - 32)
    	else:
		resultat += var


#	return ord(var) >= 97 and ord(var) <= 122




#texte = "bonjour tout le monde"
#resultat = ""

#for caractere in texte:
    # Vérifie si le caractère est une lettre minuscule (code ASCII entre 97 et 122)
#    if 97 <= ord(caractere) <= 122:
        # Soustrait 32 pour passer en majuscule
#        resultat += chr(ord(caractere) - 32)
#    else:
#        resultat += caractere

#print(resultat)  # Affiche : BONJOUR TOUT LE MONDE
