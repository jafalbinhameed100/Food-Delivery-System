from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render,redirect

from fds.models import *




# Create your views here.
class IndexView(TemplateView):
    template_name='index.html'  


class Login(TemplateView):
    template_name = 'login.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password= request.POST['password']

        user = authenticate(username=username,password=password)
        if user is not None:

            login(request,user)
            if user.last_name == '1':

                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "customer":
                    return redirect('/customer')
                else:
                    return redirect('/agent')

            else:


                return render(request,'login.html',{'message':" User Account Not Authenticated"})
        else:

            return render(request,'login.html',{'message':"Invalid Username or Password"})
        

class CustomerRegistration(TemplateView):
    template_name='c_register.html'

    def post(self , request,*args,**kwargs):
        name = request.POST['name']
        username = request.POST['username']
        phone=request.POST['phone']
        address=request.POST['address']
        email= request.POST['email']
        password = request.POST['password']
        if User.objects.filter(email=email,username=username):
            return render(request,'c_register.html',{'message':"already added the username or email"})

        else:
            user = User.objects.create_user(username=username,password=password,email=email,first_name=name,last_name='1')
            user.save()
            se = customers()
            se.user = user
            se.phone = phone
            se.address=address
            se.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "customer"
            usertype.save()


            return render(request, 'index.html', {'message': "successfully added"})