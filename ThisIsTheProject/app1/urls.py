from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name='home'),
    path("create/", views.createOrder, name='createOrder'),
    path('update/<str:pk>', views.updateOrder, name='updateOrder'),
    path('delete/<str:pk>', views.deleteOrder, name='deleteOrder'),
    path('scrap/', views.scrap, name='scrap'),
]
