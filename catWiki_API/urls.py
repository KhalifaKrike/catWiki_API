
from django.contrib import admin
from django.urls import path
from catBreeds import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.firstPage),

    path('catBreeds/', views.get_all_breeds),
    path('catBreeds/<int:id>/', views.get_breed),
    path('catBreeds_search/<str:catBreeed>/', views.cat_breed_search),
    path('popularCatBreed/', views.get_popular_breeds),

]
