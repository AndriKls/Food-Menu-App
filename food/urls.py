from django.urls import path

from food import views

app_name = 'food'  
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),  # Add a URL pattern for the item view
]
