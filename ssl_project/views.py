from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.models import User
from userprofile.models import About_us




class TestPage(TemplateView):
    template_name = "test.html"

class ThanksPage(TemplateView):
    template_name = 'index.html'

class HomePage(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if request.method == 'GET':
            if request.user.is_authenticated():
                context  = {
                    'about_us':About_us.objects.get(username__username = request.user),
                    'username_name':request.user,
                }
                return render(request, 'userprofile/detail_about_us.html' , context )

        return super(HomePage, self).get(request, *args, **kwargs)
