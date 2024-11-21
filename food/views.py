from django.http import HttpResponse
from django.shortcuts import render
from .models import Item


# Create your views here.
def index(request):
    item_list = Item.objects.all()
    return render(request, 'food/index.html',{
        'item_list': item_list,
    })

def detail(request, id):
    return render(request, 'food/item-details.html',{
        'item': Item.objects.get(id=id)})