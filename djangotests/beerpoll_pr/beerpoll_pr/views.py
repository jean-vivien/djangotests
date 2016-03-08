from django.http import HttpResponse

def racine(request):
    return HttpResponse("Racine du site Django de JV (test)")
