from django.shortcuts import render
from django.http import HttpResponse
from makeup.models import Shop

# Create your views here.

def ailinListView(request):
    shops=Shop.objects.all()
    context={
        "shoplist":shops
    }

    return render(request,"makeup/shoplist.html",context)
