from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime, timedelta

from .models import Item, ItemPurchaseHistory
from .forms import ItemForm

# Create your views here.

# Item一覧画面
class ItemIndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'items/index.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        print("*****[ItemIndexView#get_queryset]start*****")
        return Item.objects.filter(user_id=self.request.user).order_by('-id')

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

# Item購入
@login_required
def item_purchase(request, pk):
    print("*****[#item_purchase]start*****")
    item = get_object_or_404(Item, pk=pk)
    # 履歴の取得
    history_no = 0
    histories = ItemPurchaseHistory.objects.filter(item_id=item)
    if len(histories) > 0:
        histories = histories.order_by('history_no')
        # 追加する履歴の履歴番号：0開始、自分より古い履歴件数と一致
        history_no = len(histories)
        # 平均購入間隔：(最新の購入日-最古の購入日)/最新の履歴番号
        average = (datetime.today().date() - histories[0].purchase_date).days
        item.average_purchase_interval = average
        # 次回購入見込：今日+平均購入間隔
        item.next_purchase_date = datetime.today() + timedelta(days=average)
    # 履歴が0件でも共通して更新する内容
    item.last_purchase_date = datetime.today()
    item.purchase_count = history_no + 1
    item.save()

    # 履歴の登録
    history = ItemPurchaseHistory.objects.create(
        item_id = item,
        history_no = history_no,
        purchase_date = datetime.today(),
    )
    history.save()

    return redirect('apps:index')

