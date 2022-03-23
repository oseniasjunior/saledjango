from django.urls import path
from core import consumers

urlrouter = [
    path('chat/', consumers.ChatConsumer.as_asgi())
]
