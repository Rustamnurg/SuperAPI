import cgi

from django.http import HttpResponse
import datetime

# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from django.views.decorators.http import require_http_methods

from blog.models import User, Report


@require_http_methods(["GET"])
def current_datetime(request):



    reports = Report.objects.all()[0]
    # print(reports.first().base_rate)
    # RequestContext(request, {'book': book.objects.all()[0]})

    # return render('main.html', {'reports': reports})
    return render_to_response('main.html', RequestContext(request, {'reports': Report.objects.all()[0]}))


@require_http_methods(["GET"])
def signIn(request):


    email = request.GET['email']
    password = request.GET['password']


    users = User.objects.filter(email = email, password = password)
    if users.first() is not None:
        print("User is valid, active and authenticated")
        return HttpResponse("User is valid, active and authenticated")
    else:
        print("The username and password were incorrect.")
        return HttpResponse("The username and password were incorrect")
    return HttpResponse("")


@require_http_methods(["GET"])
def signUp(request):
    # return HttpResponse(rem)
    return render(request, 'blog/logIn.html', {})

@require_http_methods(["GET"])
def logout(request):
    return HttpResponse("logout")


