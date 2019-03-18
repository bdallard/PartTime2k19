## Projet POO : le polymorphisme

### Consignes 

Une boîtes aux lettres recueille des courrier qui peuvent être des lettres ou des colis.

Une lettre est caractérisée par :

son poids (en grammes)
le mode d’expédition (express ou normal)
son adresse de destination
son adresse d’expédition
son format (“A3” ou “A4”)
Un colis est caractérisé par :

son poids (en grammes)
le mode d’expédition (express ou normal)
son adresse de destination
son adresse d’expédition
son volume (en litres )
Il faut donc définir aussi les deux méthodes:

calculTimbre: qui calcule le prix du Timbre
ToString qui affiche un courrier
Règles pour calculer le prix du Timbre :

en mode d’expédition normal :

Le montant nécessaire pour affranchir une lettre dépend de son format et de son poids : Formule : montant = tarif de base + 1.0 * poids (kilos), où le tarif de base pour une lettre “A4” est de 2.50, et 3.50 pour une lettre “A3”

Le montant nécessaire pour affranchir un colis dépend de son poids et de son volume : Formule : montant = 0.25 volume (litres) + poids (kilos) 1.0

en mode d’expédition express : les montants précédents sont doublés, quelque soit le type de courrier

### Exemple d’exécution :
```
>>>L1=Lettre(“Lille”,”Paris”,80,”normal”,”A4″)
>>>L1.ToString()
Lettre:
Adresse destination: Lille 
Adress expedition: Paris
Poids: 80.00 grammes
Mode: normal 
Format:A4
Prix du timbre:0.20
>>>C1=Colis(“Marrakeche”,”Barcelone “,3500,”expresse”,2.25)
>>>C1.ToString()
Collis:
Adresse destination: Marrakeche 
Adress expedition: Barcelone 
Poids: 3500.00 grammes
Mode: expresse 
Volume: 2.25 litres
Prix du timbre:3937.50
```
