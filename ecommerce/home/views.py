from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Home, DjangoForm, FileFields
from .forms import DjangoForms, ModelForms, ImageForm

@login_required
def form(request):
    if request.method == "GET":
        name = request.GET.get('name')
        email = request.GET.get('email')
        addrs = request.GET.get('addrs')
        print(f"Name : {name}, Email : {email}, Address : {addrs}")
        return render(request, 'home/userform.html')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        addrs = request.POST.get('addrs')
        print(f"Name : {name}, Email : {email}, Address : {addrs}")
        content = {
            'name':name,
            'email':email,
            'addrs':addrs
        }
        return render(request, 'home/userform.html', content)
    else:
        return render(request, 'home/userform.html')
    
def djangoForm(request):
    if request.method == "POST":
        forms = DjangoForms(request.POST)
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        addrs = request.POST.get('Addrs')
        contact = request.POST.get('Contact')
        inserted = DjangoForm(Name=name, Phone=contact, Email=email, Address=addrs)
        inserted.save()
        print(f"""
            Name : {name}
            Email : {email}
            Address : {addrs}
            Contact : {contact}
""")
    else:
        forms = DjangoForms()
    return render(request, 'home/djangoform.html', {'forms' : forms})





@login_required
def home(request):
    data = Home.objects.all()
    content = {'datas':data}
    return render(request, 'home/index.html', content)

def details(request, item_ID):
    data_ID = Home.objects.get(pk=item_ID)
    content = {'data': data_ID}
    return render(request, 'home/details.html', content)

def ModelsForm(request):
    if request.method == 'POST':
        form = ModelForms(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('home:index')
    else:
        form = ModelForms()
    return render(request, 'home/ModelForm.html', {'forms': form})


def UpdateForm(request, item_ID):
    itemID = Home.objects.get(pk=item_ID)
    forms = ModelForms(request.POST or None, instance=itemID)
    if request.method == 'POST':
        if (forms.is_valid()):
            forms.save()
            return redirect('home:index')
    return render(request, 'home/updatepage.html', {'forms':forms})


def imageform(request):
    imgform = ImageForm(request.POST, request.FILES or None)
    if request.method == 'POST':
        
        if (imgform.is_valid()):
            imgform.save()
            return redirect('home:index')
    content = {'imgform':imgform}
    return render(request, 'home/imageform.html', content)

def allImage(request):
    datas = FileFields.objects.all()
    content = {'datas':datas}
    return render(request, 'home/allimage.html', content)