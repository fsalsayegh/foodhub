from django.contrib import admin
from .models import Restaurant, Item

class AdminFatma(admin.ModelAdmin):
	list_display =["name"]
	search_fields = ["name"]
	class Meta:
		model=Restaurant
			
admin.site.register(Restaurant, AdminFatma)
admin.site.register(Item)
