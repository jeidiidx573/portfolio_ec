from django.urls import path
from order import views

app_name = 'order'
urlpatterns = [
    path('', views.order_list, name='order_list'),
    path('form/', views.order_form, name='order_form'),
    path('conf/', views.order_conf, name='order_conf'),
    path('thanks/', views.order_thanks, name='order_thanks'),
]
