from django.urls import path
from fds.admin_views import *


urlpatterns = [

    path('',AdminIndexView.as_view()),
    path('AgentRegistration',AgentRegistration.as_view()),
    path('AgentsList',AgentsList.as_view()),
    path('AgentUpdate',AgentUpdate.as_view()),
    path('BlockAgent',BlockAgent.as_view()),
    path('UnblockAgent',UnblockAgent.as_view()),
    path('CustomerList',CustomerList.as_view()),
    path('BlockCustomer',BlockCustomer.as_view()),
    path('UnblockCustomer',UnblockCustomer.as_view()),
    path('AddProducts',AddProducts.as_view()),
    path('ProductList',ProductList.as_view()),
    path('ProductUpdate',ProductUpdate.as_view()),
    path('DeleteProduct',DeleteProduct.as_view()),
    path('OrdersDetails',OrdersDetails.as_view()),
    path('AssignOrder',AssignOrder.as_view()),
    path('UpdateStatus',UpdateStatus.as_view()),

    ]
def urls():
    return urlpatterns, 'admin', 'admin'