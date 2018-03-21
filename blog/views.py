from django.shortcuts import render

# Create your views here.
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def post_list(request):
    context_instance = RequestContext(request)
    if request.method == "POST":

        if request.method == "POST" or 'q' in request.POST:
            q = request.POST['id']
            return render(request, 'blog/post.html', {})
        else :
          return render(request, 'blog/error.html', {})

    else:
        return render(request, 'blog/get.html', {})

