from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


from . import views
app_name = "hotel"
urlpatterns = [
    path('', views.menu, name='index'),
    path('ordersummary/<int:id>/',views.orderdetails,name='orderdetails'),
    path('ordersummary/', views.ordersummary, name='ordersummary'),
    path('itemreview/', views.orderreview, name='review'),
    path('payment/', views.payment,name='pay'),
    path('payment_success/', views.assign_bonus,name='assign_bonus'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
