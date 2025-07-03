import json
from channels.generic.websocket import AsyncWebsocketConsumer # type: ignore # ✅
from channels.db import database_sync_to_async# type: ignore # ✅
from channels.auth import get_user  # type: ignore # ✅ Replaces direct use of AnonymousUser


# Async wrapper to get unread notification count
@database_sync_to_async
def get_unread_notification_count(user):
    from .models import Notification  # ✅ Safe import inside function
    return Notification.objects.filter(user=user, is_read=False).count()


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # ✅ Securely get the authenticated user from the scope
        self.user = await get_user(self.scope)

        if self.user and self.user.is_authenticated:
            self.group_name = f"notifications_{self.user.id}"

            # Add to notification group
            await self.channel_layer.group_add(
                self.group_name,
                self.channel_name
            )

            await self.accept()
            print(f"✅ WebSocket connected for {self.user}. Joined group: {self.group_name}")
        else:
            print("❌ WebSocket connection rejected. User not authenticated.")
            await self.close()

    async def disconnect(self, close_code):
        if hasattr(self, 'group_name'):
            await self.channel_layer.group_discard(
                self.group_name,
                self.channel_name
            )
            print(f"🔌 Disconnected user {self.user} from group {self.group_name}")

    async def receive(self, text_data):
        print("📩 Received message from client (not used):", text_data)
        # Placeholder for handling frontend messages if needed

    async def send_notification(self, event):
        message = event.get('message', '')

        # Safely fetch unread count
        unread_count = await get_unread_notification_count(self.user)

        # Send JSON back to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'unread_count': unread_count
        }))



