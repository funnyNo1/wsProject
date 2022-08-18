from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def wsfunc(req):
    data = json.dumps({'data':123})
    return HttpResponse(data,content_type='application/json')
