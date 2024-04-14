from django.urls import path
from . import views

urlpatterns = [
path('', views.loch_list, name='loch_list'),
path('loch/<int:id>/', views.loch_detail, name= 'loch_detail'),
]