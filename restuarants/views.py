
from django.shortcuts import render
from .models import Restaurant

def restaurant_list(request):
	objects= Restaurant.objects.all()
	context ={"items": objects}
	return render(request, "restaurant_list.html", context)

def restaurant_detail(request, restaurant_id):
	item = Restaurant.objects.get(id=restaurant_id)
	context ={"item": item}
	return render(request, "restaurant_detail.html", context)