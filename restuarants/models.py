from django.db import models
from django.db.models.signals import pre_save
from django.template.defaultfilters import slugify



class Restaurant (models.Model):
	name=models.CharField(max_length=122, unique=True)
	description = models.TextField()
	opening_time = models.TimeField()
	closing_time =models.TimeField()
	logo=models.ImageField(null=True, blank=True)
	slug= models.SlugField(blank=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering=['name']

def pre_save_res(*args, **kwargs):
	obj = kwargs['instance']
	obj.slug=slugify(obj.name)

pre_save.connect(pre_save_res, sender=Restaurant)

class Item(models.Model):
	restaurant=models.ForeignKey(Restaurant)
	name=models.CharField(max_length=122, unique=True)
	slug=models.SlugField(blank=True)
	description= models.TextField()
	price= models.DecimalField(max_digits=20, decimal_places=3)
	active= models.BooleanField(default=False)

	def __str__(self):
		return self.name

	class Meta:
		ordering=['name']


def pre_save_item(*args, **kwargs):
	objectt = kwargs['instance']
	objectt.slug=slugify(objectt.name)

pre_save.connect(pre_save_item, sender=Item)



			

