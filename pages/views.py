from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
#from django.http import request
# Create your views here.


def home_view(request, *args,**kwargs):

    '''print(args,kwargs)'''


    #return HttpResponse("<h1>Hello world </h1> <h2>by NaliN</h2> <body bgcolor = 'CAA6F8'> first page </body>")
    return render(request, "home.html")


def contact_view(request,*args,**kwargs):
    my_context = {
        "name": "NaliN Deepan",
        "Location": "Jodhpur"
    }
    return render(request, "contacts.html", my_context)