
from django.shortcuts import render , redirect
from .models import Restaurant
from .forms import RestaurantForm

def restaurant_list(request):
	objects= Restaurant.objects.all()
	context ={"items": objects}
	return render(request, "restaurant_list.html", context)

def restaurant_detail(request, restaurant_id):
	item = Restaurant.objects.get(id=restaurant_id)
	context ={"item": item}
	return render(request, "restaurant_detail.html", context)

def restaurant_create(request):
    form = RestaurantForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("restaurant_list")
    context = {
    "form": form}
    return render(request, 'restaurant_create.html', context)

def restaurant_update(request, restaurant_id):
    instance = Restaurant.objects.get(id=restaurant_id)
    form = RestaurantForm(request.POST or None, instance = instance)
    if form.is_valid():
        form.save()
        return redirect("restaurant_detail", restaurant_id=instance.id)
    context = {
    "form":form,
    "instance": instance}
    return render(request, 'restaurant_update.html', context)

def restaurant_delete(request, restaurant_id):
    instance = Restaurant.objects.get(id=restaurant_id)
    instance.delete()
    return redirect("restaurant_list")



