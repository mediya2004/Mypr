
from django.shortcuts import render,redirect
from django.contrib import messages
from.forms import  loginform,updateForm,ChangepasswordForm, registrationform1
from.models import gallery, registrationform
from django.contrib.auth import logout as logouts

from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request,'index.html')

def registrationforfun(request):
    if request.method=='POST':
        forms=registrationform1(request.POST,request.FILES)
        if forms.is_valid():
            name=forms.cleaned_data['name']
            age=forms.cleaned_data['age']
            profile=forms.files['profile']
            place=forms.cleaned_data['place']
            email=forms.cleaned_data['email']
            password=forms.cleaned_data['password']
            confirmpassword=forms.cleaned_data['ConfirmPassword']

            user=registrationform.objects.filter(email=email).exists()
            if user:
                messages.warning(request,'Email Alredy exist')
                return redirect('/login')
            elif password!=confirmpassword:
                messages.warning(request,'Password Mismatch')
            else:
                tab=registrationform(name=name,age=age,place=place,email=email,profile=profile,password=password)
                tab.save()


                subject = 'welcome to abc..'
                message = f'Hi {name}, thank you for registering in abc'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email, ]
                send_mail( subject, message, email_from, recipient_list )




                messages.success(request,'DATA SAVED')
            return redirect('/')
    else:
        forms=registrationform1()
    return render(request,'registrationforfun.html',{'forms':forms})


def login(request):
    if request.method=='POST':
        forms=loginform(request.POST)
        if forms.is_valid():
            email=forms.cleaned_data['email']
            password=forms.cleaned_data['password']
            try:
                user=registrationform.objects.get(email=email)
                if not user:
                    messages.warning(request,'email does not exist')
                    return redirect('/login')
                elif password!=user.password:
                    pass
                    return redirect('/login')
                else:
                    messages.success(request,'Success')
                    return redirect('/home/%s' % user.id)
            except:
                messages.warning(request,'Email or Password incorrect')
                return redirect('/login')
    else:
        forms=loginform()
    return render(request,'login.html',{'forms':forms})


def home(request,id):
        user=registrationform.objects.get(id=id)
        return render(request,'home.html',{'user':user})

def update(request,id):
    user=registrationform.objects.get(id=id)
    if request.method=='POST':
        form=updateForm(request.POST or None,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'Success')
            return redirect('/home/%s' % user.id)
    else:
        form=updateForm(instance=user)
    return render(request,'update.html',{'user':user,'form':form})

        
        
def delete(request):
    user=registrationform.objects.get(id=id)
    user.delete()
    messages.success(request,'SUCCESS')
    return redirect('/')


def logout(request):
    logouts(request)
    messages.success(request,'SUCCESS')
    return redirect('/')


def changepassword(request,id):
     user=ChangepasswordForm.objects.get(id=id)
     if request.method=='POST':
        forms=registrationform1(request.POST or None)
        if forms.is_valid():
            oldpassword=forms.cleaned_data['OldPassword']
            newpassword=forms.cleaned_data['NewPassword']
            Confirmpassword=forms.cleaned_data['ConfirmPassword']
            if oldpassword!=user.Password:
                 messages.warning(request,"incorrect")
                 return redirect('/changepassword/%s' % user.id)
            elif oldpassword==newpassword:
                messages.warning(request,"password similar")
            elif newpassword!=Confirmpassword:
                messages.warning(request,"password new")
                return redirect('/changepassword/%s' % user.id)
            else:
                user.Password=newpassword
                user.save()
                messages.success(request,"password changed")
        else:
            forms=ChangepasswordForm()
            return render(request,'changepassword.html',{'users':user,'forms':forms})
        
        
def logout(request):
    logouts(request)
    messages.success(request,"logged out")
    return redirect('/')

def gallery1(request):
     images=gallery.objects.all()
     return render(request,'gallery.html',{'images':images})


def details(request,id):
    images=gallery.objects.get(id=id)
    return render(request,'details.html',{'images':images})