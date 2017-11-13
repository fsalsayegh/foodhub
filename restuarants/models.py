from django.db import models

class Restaurant (models.Model):
	name=models.CharField(max_length=122)
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time =models.TimeField()
	logo=models.ImageField(null=True, blank=True)




	def __str__(self):
		return self.name

	class Meta:
		ordering=['name']
			

