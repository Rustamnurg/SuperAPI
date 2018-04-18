import json
import datetime

from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from models import *

from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
@require_http_methods(["POST"])
def post_list(request):
    context_instance = RequestContext(request)
    if request.method == "POST":

        body_unicode = request.body.decode('UTF-8')
        body_data = json.loads(body_unicode)

        if 'device_id' in body_data and 'window_id' in body_data and  'message' in body_data and 'view_name' in body_data and 'heatmap_base64' in body_data and 'base_rate' in body_data and 'api_key' in body_data and 'views_blocks' in body_data:
            device_id = body_data['device_id']
            window_id = body_data['window_id']
            message = body_data['message']
            view_name = body_data['view_name']
            heatmap_base64 = body_data['heatmap_base64']
            base_rate = body_data['base_rate']
            api_key = body_data['api_key']
            views_blocks = body_data['views_blocks']

            print(App.objects.all().first().user.first_name)
            App.objects.all()

            app = App.objects.filter(app_apikey = api_key)
            if app.first() is not None:
                newApp = App.objects.create(app_apikey=api_key, app_name="Test app name",
                                            user=User.objects.all().first())
                newApp.save()

                # new views_blocks

                newReport = Report.objects.create(app= app.first(), device_id=device_id, windows_id=window_id, message=message,
                                                  view_name=view_name, base_rate=base_rate,
                                                  created_date=datetime.datetime.now())
                # heatmap_base64

                newReport.save()
                print(views_blocks)
                return render(request, 'blog/post.html', {})
            else: return render(request, 'blog/error.html', {})




        else :
         return render(request, 'blog/error.html', {})
    else:
        return render(request, 'blog/main.html', {})

