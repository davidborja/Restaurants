from django.conf.urls import  url
from rest_framework.urlpatterns import format_suffix_patterns
from app import views



urlpatterns = [
    #url(r'^', include('restaurants.urls')),
    # url que despliega todos los restaurantes en la base de datos
    # Restaurants/
    url(r'^Restaurants/$', views.Restaurants_list.as_view()),
    # url que hace un CRUD sobre el id del restaurante
    # Restaurants/pk=301
    url(r'^Restaurants/pk=(?P<pk>[0-9]+)$', views.Restaurants_detail.as_view()),
    # url que hace la parte estadistica en base a la longitud, latitud y el radio
    # Restaurants/statics/latitude=2&longitude=2&radius=200000000 
    url(r'^Restaurants/statics/latitude=(?P<latitude>.+)&longitude=(?P<longitude>.+)&radius=(?P<radius>.+)$',views.Statics.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
