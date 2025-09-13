from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, India is a great country!")

def health_check(request):
    return HttpResponse("OK", status=200)