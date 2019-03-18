from models.Courrier import Courrier

class Lettre(Courrier, object):
	def __init__(self, format, *args):
		super(Lettre, self).__init__(*args)
		self.format = format

	def calculTimbre(self):
		prix_base = 2.50 if self.format == "A4" else 3.50
		prix_timbre = prix_base + 1 * self.poids
		return prix_timbre * 2 if self.mode_expedition == "express" else prix_timbre
   
   