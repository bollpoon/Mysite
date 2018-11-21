from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def loginOK(request):
    return render(request,'loginOK.html')
def login(request):
    account = request.POST.get('account')
    password = request.POST.get('password')
    if account == '2016210402086' and password == '123456':
        return render(request, 'loginOK.html')
    else:
        return render(request, 'login.html', {
            'account': account,
            'password': password
        })

def circle(request):
    return render(request,'circle.html')

def add(request):
    return render(request,'add.html')
    
def message(request):
    return render(request,'message.html')

def box(request):
    return render(request,'box.html')

def _self(request):
    return render(request,'_self.html')
    

