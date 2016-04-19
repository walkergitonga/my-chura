from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from .forms import LoginForm 
from forms import RegistrationForm 
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf

# Create your views here.
def login(request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/accounts/loggedin')
            else:
                message = "Invalid username and/or password, please reenter"
    
    		#limit login to only active users
    		#if user.is_active:
			#   auth.login(request, user)
			#   return HttpResponseRedirect('/accounts/loggedin')
			#else:
			#   message = "Your account is inactive"

    else:
        form = LoginForm()
    return render_to_response('registration/login.html', {'message': message, 'form': form},
                             context_instance=RequestContext(request))

def loggedin(request):
    return render_to_response('registration/loggedin.html',
    	{'username': request.user.username})

def logout(request):
    auth.logout(request)
    return render_to_response('registration/logged_out.html')

@login_required 
def restricted(request):
    return render_to_response('restricted.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register/complete')

    else:
        form = RegistrationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration/registration_form.html', token)

def registration_complete(request):
    return render_to_response('registration/registration_complete.html')


