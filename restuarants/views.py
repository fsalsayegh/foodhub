
from django.shortcuts import render , redirect
from .models import Restaurant , Item
from .forms import RestaurantForm , ItemForm ,UserSignup , UserLogin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from django.contrib import messages
from django.utils import timezone 
from datetime import datetime
from django.contrib.auth import login, logout, authenticate



def restaurant_list(request):
	objects= Restaurant.objects.all()

	query= request.GET.get('s')
	if query:
		objects=objects.filter(name__icontains=query)
			

	paginator= Paginator(objects,3)
	number=request.GET.get('page')

	try:
		objects=paginator.page(number)
	except PageNotAnInteger:
		
		objects = paginator.page(1)
	except EmptyPage:
		
		objects = paginator.page(paginator.num_pages)

	context ={"items": objects}
	return render(request, "restaurant_list.html", context)



def restaurant_detail(request, restaurant_slug):
	today= datetime.now().time()
	status = "open"

	instance = Restaurant.objects.get(slug=restaurant_slug)
	items=Item.objects.filter(restaurant=instance)

	if not request.user.is_staff:
		items = items.filter(active=True)
	if today < instance.opening_time or today > instance.closing_time:
			status = "closed"
			

	context ={
		"items": items,
		"restaurant": instance,
		"status": status
	}
	return render(request, "restaurant_detail.html", context)

def restaurant_create(request):
	if not (request.user.is_staff):
	   raise Http404

	form = RestaurantForm(request.POST or None , request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect("restaurant_list")
	context = {
	"form": form}
	return render(request, 'restaurant_create.html', context)

def restaurant_update(request, restaurant_slug):
	if not (request.user.is_staff):
	   raise Http404

	instance = Restaurant.objects.get(slug=restaurant_slug)
	form = RestaurantForm(request.POST or None, request.FILES or None, instance = instance)
	if form.is_valid():
		form.save()
		return redirect("restaurant_detail", restaurant_slug=instance.slug)
	context = {
	"form":form,
	"instance": instance}
	return render(request, 'restaurant_update.html', context)

def restaurant_delete(request, restaurant_slug):
	if not (request.user.is_staff):
	   raise Http404

	instance = Restaurant.objects.get(slug=restaurant_slug)
	instance.delete()
	return redirect("restaurant_list")





def item_create(request):
	if not (request.user.is_staff):
	   raise Http404

	form = ItemForm(request.POST or None )
	if form.is_valid():
		form.save()
		return redirect("restaurant_list")
	context = {
	"form": form}
	return render(request, 'item_create.html', context)



def item_update(request, item_slug):
	if not (request.user.is_staff):
	   raise Http404

	instance = Item.objects.get(slug=item_slug)
	form = ItemForm(request.POST or None, instance = instance)
	if form.is_valid():
		form.save()
		return redirect("restaurant_list")
	context = {
	"form":form,
	"instance": instance}
	return render(request, 'item_update.html', context)




def item_delete(request, item_slug):
	if not (request.user.is_staff):
	   raise Http404

	instance = Item.objects.get(slug=item_slug)
	instance.delete()
	messages.warning(request, "deleted")
	return redirect("restaurant_list")


def usersignup(request):
	context={}
	form= UserSignup()
	context["form"]=form

	if request.method=="POST":
		form=UserSignup(request.POST)
		if form.is_valid():
			user=form.save()

			username=user.username
			password=user.password

			user.set_password(password)
			user.save()
			auth=authenticate(username=username, password=password)
			login(request, auth)
			messages.success(request, "you have successfuly signed up.") 
			return redirect('restaurant_list')
		messages.error(request, form.errors)
	return render(request, "usersignup.html", context)


def userlogin(request):
	context={}
	form= UserLogin()
	context["form"]=form

	if request.method=="POST":
		form=UserLogin(request.POST)
		if form.is_valid():

			username=form.cleaned_data['username']
			password=form.cleaned_data['password']

			auth=authenticate(username=username, password=password)
			if auth is not None:
				login(request, auth)
				messages.success(request, "you have successfuly logged in.") 
				return redirect('restaurant_list')
			messages.error(request, "username/password combination was incorrect.")
			return redirect('userlogin')
		messages.error(request, form.errors)
	return render(request, "userlogin.html", context)

def userlogout(request):
	logout(request)
	return redirect('userlogin')




