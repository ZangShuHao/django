from django.shortcuts import render
from leongGoods.models import *


# Create your views here.
def index(request):
    a = GoodsInfo.objects.filter(gtype=1)
    return render(request, 'index.html', {'a': a})


def cart(request):
    return render(request, 'cart.html')


def detail(request):
    return render(request, 'detail.html')
