from django.db import models
from django.utils.translation import gettext_lazy as _

from characters.models import Character

class Die(models.Model):
	character = models.ForeignKey(
		Character,
		related_name="dice",
		verbose_name=_("Character"),
		on_delete=models.CASCADE,
	)
	
	@property
	def number_of_sides(self):
		return len(self.sides.all())
		
	@property
	def number_of_pips(self):
		number = 0
		for side in self.sides.all():
			number = number + side.pips
		return number
	

class Die_Side(models.Model):

	pips = models.IntegerField(
		verbose_name=_("Pips")
	)
	
	die = models.ForeignKey(
		Die,
		related_name="sides",
		verbose_name=_("Die"),
		on_delete=models.CASCADE,
	)

