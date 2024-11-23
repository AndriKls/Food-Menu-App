from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Item
from django.views.generic.edit import FormView
from .forms import ItemForm
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.

class Index(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'


class Detail(DetailView):
    model = Item
    template_name = 'food/item-details.html'
    context_object_name = 'item'



class AddItemView(CreateView):
    model = Item
    fields = ['item_name', 'item_description', 'item_price', 'item_image', 'item_full_description'  ]
    template_name = 'food/add_item.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    

def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/add_item.html', {'form': form, 'item': item})


def delete_item(request, id):
    item = Item.objects.get(id=id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html', {'item': item})