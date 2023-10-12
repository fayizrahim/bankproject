from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib import messages

from .forms import PersonCreationForm
from .models import district, branch, persondetails


# Create your views here.
def index(request):
    return render(request, 'home.html')


# def formreq(request):
# return render(request,'form.html')


def newpage(request):
    return render(request, template_name='newpage.html')


def loginn(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('newpage')
        else:
            messages.info(request, "invalid login")
            return redirect('register')

    return render(request, 'login.html')


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST['password']
        password2 = request.POST['password2']

        if password== password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();

        else:
            messages.info(request, "password not matching")
            return redirect('register')

        return redirect('login')
    return render(request,"register.html")








    # forms


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "application submitted")
            return redirect('person_add')
    return render(request, 'form.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(persondetails, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            messages.info(request, "application submited")
            return redirect('person_change', pk=pk)
    return render(request, 'form.html', {'form': form})


# AJAX
def load_cities(request):
    district_id = request.GET.get('district_id')
    branches = branch.objects.filter(district_id=district_id).all()
    return render(request, 'city_dropdown_list_options.html', {'branches': branches})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)


def logout(request):
    auth.logout(request)

    return redirect('login')
