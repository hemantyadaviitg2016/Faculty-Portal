from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from ssl_project import settings
from userprofile.models import About_us
import json
import urllib


from . import forms

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:

                recaptcha_response = request.POST.get('g-recaptcha-response')
                url = 'https://www.google.com/recaptcha/api/siteverify'
                values = {
                    'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                    'response': recaptcha_response
                }
                data = urllib.parse.urlencode(values).encode()
                req =  urllib.request.Request(url, data=data)
                response = urllib.request.urlopen(req)
                result = json.loads(response.read().decode())

                if result['success']:
                    login(request, user)
                    try:
                        return redirect('userprofile:profile_about_us' , slug=request.user)
                    except:
                        return redirect('userprofile:profile_about_us_create')
                else:
                    return render(request, 'accounts/login.html', {'error_message': 'Invalid Captcha'})


            else:
                return render(request, 'accounts/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'accounts/login.html', {'error_message': 'Invalid login'})
    return render(request, 'accounts/login.html')
