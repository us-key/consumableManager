from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Item

# Create your views here.
class ItemIndexView(generic.ListView):
    template_name = 'items/index.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        """Return the last five items"""
        return Item.objects.order_by('-id')
    
class ItemDetailView(generic.DetailView):
    model = Item
    template_name = 'items/detail.html'

def itemCreate(request):
    name = request.POST['name']
    # TODO 他カラムの取得

