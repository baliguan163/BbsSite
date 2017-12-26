from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from . models import bbs

#
# def index(request):
#     return render(request, 'index.html')

def index(request):
    bbs_list= bbs.objects.order_by('-publish_date')[:5]
    context = {'bbs_list': bbs_list}
    print(bbs_list)
    return render(request, 'index.html', context)
