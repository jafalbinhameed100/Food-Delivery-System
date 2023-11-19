from django.views.generic import TemplateView,View
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import logout

from fds.models import *

# Create your views here.

class AdminIndexView(TemplateView):
    template_name='admin/index.html'


class AgentRegistration(TemplateView):
    template_name='admin/a_register.html'
    def post(self , request,*args,**kwargs):
        name = request.POST['name']
        username = request.POST['username']
        phone=request.POST['phone']
        address=request.POST['address']
        email= request.POST['email']
        password = request.POST['password']
        image=request.FILES['image']
        fii=FileSystemStorage()
        filesss=fii.save(image.name,image)
        if User.objects.filter(email=email,username=username):
            return render(request,'admin/index.html',{'message':"already added the username or email"})

        else:
            user = User.objects.create_user(username=username,password=password,email=email,first_name=name,last_name='1')
            user.save()
            se = agents()
            se.user = user
            se.phone = phone
            se.address=address
            se.image=filesss
            se.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "agent"
            usertype.save()
            return render(request, 'admin/index.html', {'message': "successfully added"})
        

class AgentsList(TemplateView):
    template_name='admin/d_agents_list.html'
    def get_context_data(self, **kwargs):
        context = super(AgentsList,self).get_context_data(**kwargs)

        agent = agents.objects.all()

        context['agent'] = agent
        return context
    
class AgentUpdate(TemplateView):
    template_name = 'admin/update_agents.html'
    def get_context_data(self, **kwargs):
        id = self.request.GET['id']
        context = super(AgentUpdate,self).get_context_data(**kwargs)
        agent = agents.objects.filter(user_id=id)

        context['agent'] = agent
        return context
    
    def post(self,request,*args,**kwargs):
        id = request.POST['id']
        image=request.FILES['image']
        fii=FileSystemStorage()
        filesss=fii.save(image.name,image)

        usr = agents.objects.get(user_id=id)
        usr.address = request.POST['address']
        usr.phone = request.POST['phone']
        usr.image=filesss
        usr.save()
        agt=User.objects.get(id=id)
        agt.first_name = request.POST['name']
        agt.email = request.POST['email']
        agt.username = request.POST['username']
        agt.save()
        return render(request,'admin/index.html',{'message':"Updated"})
    
class BlockAgent(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.is_active='0'
        user.save()
        return render(request,'admin/index.html',{'message':"Account Blocked"})

class UnblockAgent(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(id=id)
        user.is_active='1'
        user.save()
        return render(request,'admin/index.html',{'message':"Account Unblocked"})
    
class CustomerList(TemplateView):
    template_name='admin/customer_list.html'
    def get_context_data(self, **kwargs):
        context = super(CustomerList,self).get_context_data(**kwargs)

        cust = customers.objects.all()

        context['cust'] = cust
        return context
    
class BlockCustomer(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.is_active='0'
        user.save()
        return render(request,'admin/index.html',{'message':"Account Blocked"})

class UnblockCustomer(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(id=id)
        user.is_active='1'
        user.save()
        return render(request,'admin/index.html',{'message':"Account Unblocked"})
    
class AddProducts(TemplateView):
    template_name = 'admin/add_products.html'
    def post(self , request,*args,**kwargs):
        name = request.POST['name']
        category = request.POST['category']
        price=request.POST['price']
        image=request.FILES['image']
        fii=FileSystemStorage()
        filesss=fii.save(image.name,image)
        
        se = products()
        se.name = name
        se.category = category
        se.price=price
        se.image=filesss
        se.status='added'
        se.save()
        
        return render(request, 'admin/index.html', {'message': "successfully added"})
    
class ProductList(TemplateView):
    template_name='admin/product_list.html'
    def get_context_data(self, **kwargs):
        context = super(ProductList,self).get_context_data(**kwargs)

        product = products.objects.all()

        context['product'] = product
        return context
    
class ProductUpdate(TemplateView):
    template_name = 'admin/update_product.html'
    def get_context_data(self, **kwargs):
        id = self.request.GET['id']
        context = super(ProductUpdate,self).get_context_data(**kwargs)
        product = products.objects.filter(id=id)

        context['product'] = product
        return context
    
    def post(self,request,*args,**kwargs):
        id = request.POST['id']
        image=request.FILES['image']
        fii=FileSystemStorage()
        filesss=fii.save(image.name,image)

        usr = products.objects.get(id=id)
        usr.name = request.POST['name']
        usr.price = request.POST['price']
        usr.category = request.POST['category']
        usr.image=filesss
        usr.save()
       
        return render(request,'admin/index.html',{'message':"Updated"})
    
class DeleteProduct(View):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        products.objects.get(id=id).delete()
        return render(request,'admin/index.html',{'message':"Removed"})

class OrdersDetails(TemplateView):
    template_name= 'admin/orders.html'
    def get_context_data(self, **kwargs):
        context = super(OrdersDetails, self).get_context_data(**kwargs)
       
        pr = cart.objects.all()
        context['pr'] = pr

        return context
    
class AssignOrder(TemplateView):
    template_name='admin/assign_order.html'
    def get_context_data(self, **kwargs):
        context = super(AssignOrder,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        order = cart.objects.get(id=id)
        agent = agents.objects.all()

        context['agent'] = agent
        context['order'] = order
        return context
    
    def post(self, request, *args, **kwargs):
        # id = self.request.GET['id']
        id=request.POST['id']
        agent = request.POST['agent']
        se=assign()
        se.agent_id=agent
        se.crt_id=id
        se.status='assigned'
        se.save()
        # id=request.GET['id']
        feed =cart.objects.get(id=id)
        feed.status='assigned'
        feed.save()
        return render(request, 'admin/index.html', {'message': "Assigned to delivery agent"})
    
class UpdateStatus(TemplateView):
    template_name = 'admin/update_status.html'
    def get_context_data(self, **kwargs):
        id = self.request.GET['id']
        context = super(UpdateStatus,self).get_context_data(**kwargs)
        asg = cart.objects.filter(id=id)

        context['asg'] = asg
        return context
    
    def post(self,request,*args,**kwargs):
        id = request.POST['id']
        usr = cart.objects.get(id=id)
        usr.status = request.POST['status']
        usr.save()
        return render(request,'admin/index.html',{'message':"Updated"})