from django.http import HttpResponse

def hello(request):
    return HttpResponse("My Custom Django App says Hello!")

def health_check(request):
    return HttpResponse("OK, the service is healthy", status=200)