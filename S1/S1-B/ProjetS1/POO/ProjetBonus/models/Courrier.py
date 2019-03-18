from pprint import pprint

class Courrier:
	def __init__(self, poids, adresse_destination, adresse_expedition, mode_expedition="normal"):
		self.poids = poids
		self.mode_expedition = mode_expedition
		self.adresse_destination = adresse_destination
		self.adresse_expedition = adresse_expedition

	def ToString(self):
		pprint(vars(self))
		print "Prix timbre: " + str(self.calculTimbre())

	def calculTimbre(self):
		pass