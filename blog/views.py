from django.shortcuts import render

# Create your views here.
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def post_list(request):
    context_instance = RequestContext(request)
    if request.method == "POST":

        if 'id_device' in request.POST and 'token' in request.POST and \
                'window_id' in request.POST and 'view_id' in request.POST and 'rate' in request.POST :
            id_device = request.POST['id_device']
            token = request.POST['token']
            window_id = request.POST['window_id']
            view_id = request.POST['view_id']
            rate = request.POST['rate']
            print(id_device)

            return render(request, 'blog/post.html', {})
        else :
          return render(request, 'blog/error.html', {})

    else:
        return render(request, 'blog/get.html', {})

