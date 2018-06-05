import json
import datetime
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from blog.models import *
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import base64
import uuid


@csrf_exempt
@require_http_methods(["POST"])
def report(request):
    context_instance = RequestContext(request)
    if request.method == "POST":

        body_unicode = request.body.decode('UTF-8')
        body_data = json.loads(body_unicode)

        if 'device_id' in body_data and 'window_id' in body_data and 'message' in body_data and 'view_name' in body_data and 'heatmap_base64' in body_data and 'base_rate' in body_data and 'api_key' in body_data and 'views_blocks' in body_data and 'uudid' in body_data:
            device_id = body_data['device_id']
            window_id = body_data['window_id']
            message = body_data['message']
            view_name = body_data['view_name']
            heatmap_base64 = body_data['heatmap_base64']
            uudid = body_data['uudid']
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
                image_name = uuid.uuid4().hex

                newReport = Report.objects.create(app= app.first(), device_id=device_id, windows_id=window_id, message=message,
                                                  view_name=view_name, base_rate=base_rate,
                                                  created_date=datetime.datetime.now(), uudid = uudid, image_name = image_name)


                img_data = heatmap_base64
                with open("/home/superapi/SuperAPI/blog/images/{0}.png".format(image_name), "wb") as fh:
                    fh.write(img_data.decode('base64'))

                newReport.save()
                print(views_blocks)
                return render(request, 'api/post.html', {})
            else: return render(request, 'api/error.html', {})

        else :
         return render(request, 'api/error.html', {})
    else:
        return render(request, 'api/error.html', {})

