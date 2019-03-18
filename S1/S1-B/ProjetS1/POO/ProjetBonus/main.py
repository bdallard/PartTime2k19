#Python version 2.7.13
from models.Lettre import Lettre
from models.Colis import Colis

lettre = Lettre(
	'A3', 
	35.00,
	'Paris',
	'Rome',
);

colis = Colis(
	1.30, 
	35.00,
	'Paris',
	'Rome',
	'express'
);

print '\n'
lettre.ToString()
print '\n'
colis.ToString()