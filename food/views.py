from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Item
from django.views.generic.edit import FormView
from .forms import ItemForm
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    item_list = Item.objects.all()
    return render(request, 'food/index.html',{
        'item_list': item_list,
    })

def detail(request, id):
    return render(request, 'food/item-details.html',{
        'item': Item.objects.get(id=id)})


class AddItemView(FormView):
    form_class = ItemForm
    template_name = 'food/add_item.html'
    success_url = reverse_lazy('food:index')


    def form_valid(self, form):
        form.save()
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