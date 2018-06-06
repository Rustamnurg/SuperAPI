import uuid
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext, loader
from django.views.decorators.csrf import csrf_protect

from django.views.decorators.http import require_http_methods
from blog.models import *



@require_http_methods(["GET"])
def current_datetime(request):
    reports = Report.objects.all()
    template = loader.get_template('main/main.html')
    context = {
        'reports': reports,
    }
    return HttpResponse(template.render(context))

@require_http_methods(["GET"])
def my(request):
    if 'email' in request.COOKIES:
        print(request.COOKIES['email'])
        users = User.objects.filter(email=request.COOKIES['email'])
        if users.first() is not None:
            user = users.first()
            apps = App.objects.filter(user = user)
            if apps.first() is not None:
                app = apps.first()
                reports = Report.objects.filter(app = app)
                template = loader.get_template('main/my.html')
                context = {
                    'reports': reports,
                    'app': app
                }
                return HttpResponse(template.render(context))

            else:
                print("NOT app")
                response = redirect('/enterAppName')
                return response
        else:
         print("NOT user")
         response = redirect('/logIn')
         return response

    else:
        print("NOT email")
        response = redirect('/logIn')
        return response


@csrf_protect
def signIn(request):
    if request.method == "POST":
         email = request.POST['email']
         password = request.POST['password']
         users = User.objects.filter(email = email, password = password)
         if users.first() is not None:
            response = redirect('/my')
            response.set_cookie('email', email)
            return response
         else:
            print("The username and password were incorrect.")
            return HttpResponse("The username and password were incorrect")

    else:
        return render(request, 'authorization/singIn.html', {})




@csrf_protect
def signUp(request):
    if request.method == "POST":
         email = request.POST['email']
         #TODO validation
         password = request.POST['password']
         conformationPassword = request.POST['conformation_password']

         users = User.objects.filter(email = email)

         if users.first() is not None:
            print("User is valid, active and authenticated")
            return HttpResponse("User is valid, active and authenticated")
         else:
            newUser = User.objects.create(email = email, password = password)
            newUser.save()
            response = redirect('/my')
            response.set_cookie('email', email)
            return response
    else:
        return render(request, 'authorization/singUp.html', {})



@require_http_methods(["GET"])
def logout(request):
    response = redirect('/signIn')
    response.delete_cookie('email')
    return response



@csrf_protect
def enterAppName(request):
    if request.method == "POST":
         appName = request.POST['appName']

         if 'email' in request.COOKIES:
             print(request.COOKIES['email'])
             users = User.objects.filter(email=request.COOKIES['email'])
             if users.first() is not None:
                 user = users.first()

                 apps = App.objects.filter(user=user)
                 if apps.first() is None:
                     newApp = App.objects.create(user=user, app_apikey=uuid.uuid4().hex, app_name=appName)
                     newApp.save()

                 response = redirect('/my')
                 return response

             else:
                 print("NOT user")
                 response = redirect('/logIn')
                 return response

         else:
             print("NOT email")
             response = redirect('/logIn')
             return response
    else:
        return render(request, 'main/appCreate.html', {})


@require_http_methods(["GET"])
def test(request):
    xdata = ["Apple", "Apricot", "Avocado", "Banana", "Boysenberries", "Blueberries", "Dates", "Grapefruit", "Kiwi",
             "Lemon"]
    ydata = [52, 48, 160, 94, 75, 71, 490, 82, 46, 17]
    chartdata = {'x': xdata, 'y': ydata}
    charttype = "pieChart"
    chartcontainer = 'piechart_container'
    data = {
        'charttype': charttype,
        'chartdata': chartdata,
        'chartcontainer': chartcontainer,
        'extra': {
            'x_is_date': False,
            'x_axis_format': '',
            'tag_script_js': True,
            'jquery_on_ready': False,
        }
    }
    return render_to_response('main/test.html', data)
