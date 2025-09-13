from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, India is a beautiful country which is known for its diverse culture and heritage!")

def health_check(request):
    return HttpResponse("OK", status=200)