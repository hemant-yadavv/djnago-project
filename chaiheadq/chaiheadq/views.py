from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello World. You are at Django Home Page")