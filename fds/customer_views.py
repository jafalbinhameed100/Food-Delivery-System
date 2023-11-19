from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage

from fds.models import *

# Create your views here.
class CustomerIndexView(TemplateView):
    template_name='customer/index.html'  
    def get_context_data(self, **kwargs):
        context = super(CustomerIndexView,self).get_context_data(**kwargs)

        product = products.objects.all()

        context['product'] = product
        return context

class ProductDetails(TemplateView):
    template_name = 'customer/products_details.html'
    def get_context_data(self, **kwargs):
        context = super(ProductDetails,self).get_context_data(**kwargs)
        id= self.request.GET['id']
        pr = products.objects.filter(id=id)
        
        context['pr'] = pr
        return context
    
    def post(self , request,*args,**kwargs):
        user=customers.objects.get(user_id=self.request.user.id)
        quantity=request.POST['quantity']
        id= self.request.GET['id']
        pr = products.objects.get(id=id)
        price=pr.price
        Total= int(quantity)*int(price)

        se = cart()
        se.user_id=user.id
        se.product_id=pr.id
        se.quantity=quantity
        se.status='pending'
        se.total=Total
        se.save()
        
        return render(request, 'customer/index.html', {'message': "successfully added"})
    

class ViewCart(TemplateView):
    template_name = 'customer/cart_view.html'
    def get_context_data(self, **kwargs):
        context = super(ViewCart, self).get_context_data(**kwargs)
        user=customers.objects.get(user_id=self.request.user.id)

        ct = cart.objects.filter(status='pending', customer_id=user.id)
       

        total = 0
        for i in ct:
            total = total + int(i.total)

        context['ct'] = ct
        context['asz'] = total

        return context
    
class RemovecartView(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        cart.objects.get(id=id).delete()


        return redirect(request.META['HTTP_REFERER'])
    
class checkout(TemplateView):
    template_name = 'customer/payment.html'
    def get_context_data(self, **kwargs):
        context = super(checkout, self).get_context_data(**kwargs)
        # user = User.objects.get(id=self.request.user.id)
        # id =self.request.GET['id']

        user=customers.objects.get(user_id=self.request.user.id)


        ct = cart.objects.filter(status='pending', customer_id=user.id)

        total = 0
        for i in ct:
            total = total + int(i.total)

        context['ct'] = ct
        context['asz'] = total

        return context

class payment(TemplateView):
    template_name= 'user/payment.html'
    def dispatch(self,request,*args,**kwargs):

        user=customers.objects.get(user_id=self.request.user.id)


        ch = cart.objects.filter(customer_id=user.id,status='pending')


        print(ch)
        
        for i in ch:
            i.status='paid'
            i.payment='paid'
            i.save()

        return render(request,'customer/index.html',{'message':" payment Successfull, Check Booking Details"})

class OrdersDetails(TemplateView):
    template_name= 'customer/orders.html'
    def get_context_data(self, **kwargs):
        context = super(OrdersDetails, self).get_context_data(**kwargs)
        user=customers.objects.get(user_id=self.request.user.id)
        pr = cart.objects.filter(customer_id=user.id)
        context['pr'] = pr

        return context

class CancelOrder(TemplateView):
    def dispatch(self,request,*args,**kwargs):
        id = request.GET['id']
        ct=cart.objects.get(id=id)
        ct.status="cancelled"
        ct.save()
        return redirect(request.META['HTTP_REFERER'])
    