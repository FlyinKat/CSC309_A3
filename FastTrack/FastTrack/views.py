from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('registration/login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/home')
    else:
        return HttpResponseRedirect('/invalid')

def loggedin(request):
    return render_to_response('registration/loggedin.html', {'full_name':request.user.username})


def invalid_login(request):
    return render_to_response('registration/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('registration/logout.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register_success')

    args = {}
    args.update(csrf(request))

    args['form'] = UserCreationForm()
    print args
    return render_to_response('registration/register.html', args)

def register_success(request):
    return render_to_response('registration/register_success.html')

def search_trips(request):
    return render_to_response('search/search_trips.html')

def search_jobs(request):
    return render_to_response('search/search_jobs.html')

def post_trips(request):
    return render_to_response('post/post_trips.html')

def post_jobs(request):
    return render_to_response('post/post_jobs.html')