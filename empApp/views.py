from django.shortcuts import render, redirect
from empApp.forms import EmployeeForm
from empApp.models import Employee

from django.core.paginator import Paginator

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
        employees = Employee.objects.all()
        return render(request,"index.html",{'employees':employees})

@login_required
def create(request):
        if request.method == "POST":
            form = EmployeeForm(request.POST,request.FILES)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('/show')
                except:
                    pass
        else:
            form = EmployeeForm()
        return render(request,'create.html',{'form':form})

def show(request):
        #employees = Employee.objects.all()
        # employee_list = employees
        # paginator = Paginator(employee_list, 5) # Show 5 contacts per page
        #
        # page = request.GET.get('page')
        # employees = paginator.get_page(page)

        ####################### Data Table Here #####################
        employees = Employee.objects.all()
        return render(request,"list.html",{'employees':employees})

def edit(request, id):
        employee = Employee.objects.get(id=id)
        form = EmployeeForm(request.POST,request.FILES) #try
        return render(request,'edit.html', {'employee':employee,'form':form})

def update(request, id):
        employee = Employee.objects.get(id=id)
        form = EmployeeForm(request.POST,request.FILES,instance=employee)
        if form.is_valid():
            form.save()
            return redirect("/show")
        return render(request, 'edit.html', {'employee': employee})

def destroy(request, id):
        employee = Employee.objects.get(id=id)
        employee.delete()
        return redirect("/show")

#===============================================================================
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            form.save()
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect("/show")
    else:
        form = UserCreationForm(request.POST)

    context = {'form':form}
    return render(request,'registration/register1.html',context)
