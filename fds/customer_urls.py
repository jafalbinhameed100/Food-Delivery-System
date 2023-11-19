from django.urls import path
from fds.customer_views import *


urlpatterns = [

    path('',CustomerIndexView.as_view()),
    path('ProductDetails',ProductDetails.as_view()),
    path('ViewCart',ViewCart.as_view()),
    path('RemovecartView',RemovecartView.as_view()),
    path('checkout',checkout.as_view()),
    path('payment',payment.as_view()),
    path('OrdersDetails',OrdersDetails.as_view()),
    path('CancelOrder',CancelOrder.as_view()),
    
    ]
def urls():
    return urlpatterns, 'customer', 'customer'