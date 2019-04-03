from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Item
from .forms import ItemForm

# Create your views here.

# Item一覧画面
class ItemIndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'items/index.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        print("*****[ItemIndexView#get_queryset]start*****")
        """Return the last five items"""
        return Item.objects.filter(user_id=self.request.user.id).order_by('-id')

# Item詳細画面  
class ItemDetailView(LoginRequiredMixin, generic.DetailView):
    model = Item
    template_name = 'items/detail.html'

# Item作成画面
@login_required
def item_create(request):
    print("*****[#item_create]start*****")

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user_id = request.user
            item.save()
            return redirect('apps:index')
    else:
        form = ItemForm()
        return render(request, 'items/edit.html', {'form': form})


