

from django.http import HttpResponse

def index(request):
    return HttpResponse('hello,world')

def giao(request):
    return HttpResponse('你给我的一giaogiao')