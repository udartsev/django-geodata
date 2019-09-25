from django.urls import path
from geodata import views

urlpatterns = [
    path('cities/get/first', views.FirstCity.as_view()),
    path('geodata/<str:code>/cities', views.AllCities.as_view()),
    # path('geodata/<str:code>/cities/<str:search>', views.AllCitiesSearch.as_view()),
]
