from django.urls import path
from ws.consumers import WsConsumer

websocket_urlpatterns = [
    path('ws/consumer/', WsConsumer),
]

