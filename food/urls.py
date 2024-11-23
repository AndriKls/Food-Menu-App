from django.urls import path

from food import views

app_name = 'food'  
urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('<int:pk>/', views.Detail.as_view(), name='detail'),
    path('add-item/', views.AddItemView.as_view(), name='add-item'),
    path('update/<int:id>', views.update_item, name='update-item'),
    path('delete/<int:id>', views.delete_item, name='delete-item'),
]
