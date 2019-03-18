from models.Courrier import Courrier

class Colis(Courrier, object):
	def __init__(self, volume, *args):
		super(Colis, self).__init__(*args)
		self.volume = volume

	def calculTimbre(self):
		prix_timbre = self.volume + self.poids
		return prix_timbre * 2 if self.mode_expedition == "express" else prix_timbre