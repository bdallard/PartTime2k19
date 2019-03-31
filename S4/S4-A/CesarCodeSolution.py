'''
Le chiffrement peut être représenté par la superposition de deux alphabets, l'alphabet clair présenté dans l'ordre normal et l'alphabet chiffré décalé, à gauche ou à droite, du nombre de lettres voulu.
	clair   : ABCDEFGHIJKLMNOPQRSTUVWXYZ
	chiffré : DEFGHIJKLMNOPQRSTUVWXYZABC

En commençant par transformer chaque lettre en un nombre (A = 0, B = 1,..., Z = 25), on voit que l'indexation va représenter une part importante de notre problème. 
On utilise alors la fonction ord() native de python qui permet de transformer les string en integer. 
L'utilisation de l'instruction for dans tableau est assez sympathique, elle permet un code concis. 
Attention à ne pas oublier le modulo.  
'''
def code_cesar(m):
    s = "".join( [ chr((ord(l)-65+3)%26+65) for l in m ] )
    return s


m = "JENESUISPASCODE"

print(code_cesar(m))

