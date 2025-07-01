from django.urls import re_path
from Distributor_app.dashboard import consumers

websocket_urlpatterns = [
    re_path(r"ws/notifications/$", consumers.NotificationConsumer.as_asgi()),
]

