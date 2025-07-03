from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('checkview', views.checkview, name='checkview'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('<str:room>/', views.room, name='room'),
]
