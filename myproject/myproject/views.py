from django.http import HttpResponse

def hello(request):
    return HttpResponse("My Custom App litgd !")

def health_check(request):
    return HttpResponse("OK, the service is healthy and is telling you to stop me for deploying again and again....!!!", status=200)

def top(request):
    return HttpResponse("This is the top page of the applications.")    