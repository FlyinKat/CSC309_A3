from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from ft.models import Customer, Courier
from django.template import RequestContext
from forms import MyForms
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

@login_required
def Profile(request):
    #if request.method == 'POST':
     #   form = MyForms(request.POST, instance=request.user.profile)
      #  if form.is_valid():
       #     form.save()
        #    return HttpResponseRedirect('/loggedin/')
    #else:
     #   form = MyForms(instance = request.user.profile)
    #return render_to_response('Registration/profile.html', {'user_profile': form}, context_instance=RequestContext(request))
    user_profile = request.user
    context={"user_profile":user_profile}
    return render_to_response('Registration/profile.html',context, context_instance=RequestContext(request))

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
        return HttpResponseRedirect('/loggedin')
    else:
        return HttpResponseRedirect('/invalid')

def loggedin(request):
    return render_to_response('registration/loggedin.html', {'full_name':request.user.username})

def home(request):
    return render_to_response('home/home.html', {'username':request.user.username})

def invalid_login(request):
    return render_to_response('registration/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('registration/logout.html')

def register_user(request):
    if request.method == 'POST':
        form = MyForms(request.POST)
        if form.is_valid():
            user = form.save()
            subject = 'Thank You for joining us!'
            message = 'Welcome to FastTrack, login to post an ad or search for postings to look for courier'
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            if user.regAs == '1':
                c = Customer(user=user)
                c.save()
            else:
                co = Courier(user=user)
                co.save()

            return HttpResponseRedirect('/register_success')

    args = {}
    args.update(csrf(request))

    args['form'] = MyForms()
    print (args)
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
