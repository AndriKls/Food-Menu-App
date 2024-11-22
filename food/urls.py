from django.urls import path

from food import views

app_name = 'food'  
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('add-item/', views.AddItemView.as_view(), name='add-item'),
    path('update/<int:id>', views.update_item, name='update-item'),
    path('delete/<int:id>', views.delete_item, name='delete-item'),
]
