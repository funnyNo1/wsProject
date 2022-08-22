from django.shortcuts import render
from django.http import HttpResponse
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import json
# Create your views here.

def index(request):
    return render(request, 'index.html')

def room(request, room_name):
    return render(request, 'room.html', {
        'room_name': room_name
    })

def autosend(request):
    #TODO key可以使用user_id, channels_name需要存储到redis
    channels_name = request.GET.get('channels_name')
    channels_layer = get_channel_layer()
    async_to_sync(channels_layer.send)(channels_name,{"type":"chat_message","message":"server send test"})
    data = json.dumps({'code':200})
    return HttpResponse(data,content_type='application/json')