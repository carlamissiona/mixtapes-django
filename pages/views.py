from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.urls import reverse
 
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate 

# Create your views here.
def homepage(request):
	 
    return render(request, 'pages/home.html')

def appindex(request):
     
    return render(request, 'pages/home.html')

def login(request):
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('pages:register'))
    if request.method == 'POST':
        authenticated_user = authenticate(username="root", password=request.POST['password'])
        
       
  
    return HttpResponseRedirect(reverse('api:playlist_generics'))


def register(request):
    # if request.method != 'POST':
    # else:
    #     authenticated_user = authenticate(email=request.POST['email'], password=request.POST['password1'])
    #     login(request, authenticated_user)
    #     return HttpResponseRedirect(reverse('pages:register'))
 
    return render(request, 'pages/register.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('pages:homepage'))


#def register(request):
    # if request.method != 'POST':
    #     form = UserCreationForm()
    # else:
    # 	form = UserCreationForm(data=request.POST)
    #     if form.is_valid():
    #         new_user = form.save()
    #         authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
    #         login(request, authenticated_user)
    #         return HttpResponseRedirect(reverse('pages:homepage'))
    # context = {'form': form}
    # return render(request, 'pages/register.html', context)
 
