from django.urls import path,include

from . import views

app_name = 'apps'
urlpatterns = [
    # Item
    path('items/', views.ItemIndexView.as_view(), name='index'),
    path('items/<int:pk>/', views.ItemDetailView.as_view(), name='detail'),
]