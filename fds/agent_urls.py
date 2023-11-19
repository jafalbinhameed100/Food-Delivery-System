from django.urls import path
from fds.agent_views import *


urlpatterns = [

    path('',AgentIndexView.as_view()),
    path('OrdersDetails',OrdersDetails.as_view()),
    path('UpdateStatus',UpdateStatus.as_view()),
    
    ]
def urls():
    return urlpatterns, 'agent', 'agent'