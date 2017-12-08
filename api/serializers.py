from rest_framework import serializers
from restuarants.models import Restaurant , Item

class RestaurantListSerializer(serializers.ModelSerializer):
	detail_page = serializers.HyperlinkedIdentityField(
		view_name="restaurant_detail_json",
		lookup_field="slug"
	
		)
	class Meta:
		model = Restaurant
		fields=['name', 'logo', 'opening_time' ,'closing_time' , 'detail_page' ]

class RestaurantDetailSerializer(serializers.ModelSerializer):
	items = serializers.SerializerMethodField()
	class Meta:
		model = Restaurant
		fields=['id', 'name', 'slug', 'description', 'logo','opening_time' ,'closing_time' ,'items']

	def get_items(self, obj):
		#item_list = Item.objects.filter(restaurant=obj) 
		item_list= obj.item_set.all() #displays a list of all Item objects related to this specific restaurant
		items = ItemListSerializer(item_list, many=True, context=self.context).data 
		return items

class RestaurantCreateUpdateSerializer(serializers.ModelSerializer):
	class Meta:
		model = Restaurant
		fields=[ 'name', 'description', 'logo','opening_time' ,'closing_time']


class ItemListSerializer(serializers.ModelSerializer):
	detail= serializers.HyperlinkedIdentityField(
		view_name="item_detail_json",
		lookup_field="slug")
	class Meta:
		model = Item
		fields= ['name', 'price', 'active', 'detail']

class ItemDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields= ['id', 'restaurant','name','slug', 'description', 'price', 'active']
