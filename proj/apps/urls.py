from django.urls import path,include

from . import views

app_name = 'apps'
urlpatterns = [
    # Item
    path('', views.ItemIndexView.as_view(), name='index'),
    path('items/', views.ItemIndexView.as_view(), name='index'),
    path('items/<int:pk>/', views.ItemDetailView.as_view(), name='detail'),
    path('items/new/', views.item_create, name='item_new'),
    # ItemPurchaseHistory
    path('items/<int:pk>/purchase/', views.item_purchase, name='item_purchase'),
]