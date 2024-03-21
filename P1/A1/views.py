from django.shortcuts import render,redirect
from .models import emp,User
from .forms import EmpForm,UserRegister,UserLogin
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
def addinfo(request):
    if request.method == 'POST':
        frm = EmpForm(request.POST)
        if frm.is_valid():
            frm.save()
            return HttpResponse('data store in database successfully')
    else:
        frm = EmpForm()
    return render(request,'info.html',{'frm':frm})


def showinfo(request):
    data = emp.objects.all()
    return render(request,'showinfo.html',{'data':data})

def updateinfo(request,id):
    data = emp.objects.get(id=id)
    frm = EmpForm(request.POST,instance=data)
    if frm.is_valid():
        frm.save()
        return redirect('showinfo/')
    else:
        frm = EmpForm(instance=data)
    return render(request,'update.html',{'frm':frm})

def deleteinfo(request,id):
    data = emp.objects.get(id=id).delete()
    return render(request,'show.html',{'data':data})

def signup(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login/')
    else:
        form = UserRegister()
    return render(request,'signup.html',{'form':form})

# def login(request):
#     if request.method == 'POST':
#         form = UserLogin(data=request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request,user)
#                 return redirect('showinfo/')
#     else:
#         form = UserLogin(data=request.POST)
#     return render(request,'login.html',{'form':form})

# def login(request):
#     if request.method == 'POST':
#         form = UserLogin(data=request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']
#             print(email)
#             user = authenticate(request,email=email,password=password)
#             print(user)
#             if user is not None:
#                 login(request, user)
#                 return redirect('showinfo') # Use the name of the URL pattern
#     else:
#         form = UserLogin()
#     return render(request, 'login.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = UserLogin(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('showinfo/')
    else:
        form = UserLogin()
    return render(request, 'login.html', {'form': form})

def table(request):
    data = User.objects.all()
    return render(request,'table.html',{'data': data})

def logout(request):
    logout(request)
    # return redirect('login/')
    return HttpResponse('hi')