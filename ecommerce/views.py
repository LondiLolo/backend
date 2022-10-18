from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.

def ecomView(request):
    return HttpResponse("Welcome to ecom")

# creating the CBV
class MyViews(View):
    def get(self, request):
        return HttpResponse("This is CBV")


