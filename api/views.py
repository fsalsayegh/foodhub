from rest_framework.generics import ListAPIView , RetrieveAPIView ,DestroyAPIView , CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from restuarants.models import Restaurant  

from .serializers import *

from rest_framework.filters import SearchFilter 

class RestaurantListAPIView(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListSerializer
	filter_backends = [SearchFilter,]  
	search_fields=['name', 'description']
	permission_classes = [AllowAny]



class RestaurantDetailAPIView(RetrieveAPIView):
	queryset = Restaurant .objects.all()
	serializer_class = RestaurantDetailSerializer

	lookup_field='slug'
	permission_classes = [IsAuthenticated]

class RestaurantDeleteAPIView(DestroyAPIView):
	queryset = Restaurant .objects.all()
	serializer_class = RestaurantListSerializer

	lookup_field='slug'
	permission_classes = [IsAuthenticated , IsAdminUser]

class RestaurantCreateAPIView(CreateAPIView):
	queryset = Restaurant .objects.all()
	serializer_class = RestaurantCreateUpdateSerializer

	permission_classes = [IsAuthenticated , IsAdminUser]


class RestaurantUpdateAPIView(RetrieveUpdateAPIView):
	queryset = Restaurant .objects.all()
	serializer_class = RestaurantCreateUpdateSerializer

	lookup_field='slug'
	permission_classes = [IsAuthenticated , IsAdminUser]

