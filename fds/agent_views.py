from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage

from fds.models import *

# Create your views here.

class AgentIndexView(TemplateView):
    template_name='agent/index.html'  

class OrdersDetails(TemplateView):
    template_name= 'agent/orders.html'
    def get_context_data(self, **kwargs):
        context = super(OrdersDetails, self).get_context_data(**kwargs)
        com=agents.objects.get(user_id=self.request.user.id)
        pr = assign.objects.filter(agent_id=com.id)
        context['pr'] = pr

        return context
    
class UpdateStatus(TemplateView):
    template_name = 'agent/update_status.html'
    def get_context_data(self, **kwargs):
        id = self.request.GET['id']
        context = super(UpdateStatus,self).get_context_data(**kwargs)
        asg = assign.objects.filter(id=id)

        context['asg'] = asg
        return context
    
    def post(self,request,*args,**kwargs):
        id = request.POST['id']
        usr = assign.objects.get(id=id)
        usr.status = request.POST['status']
        usr.save()
        id1 = request.POST['id1']
        crt = cart.objects.get(id=id1)
        crt.status = usr.status
        crt.save()
        return render(request,'agent/index.html',{'message':"Updated"})