from typing import List, Dict, Optional
from uuid import uuid4

from models.user import User


class Room:

    def __init__(self, room_id: str = str(uuid4()), users: List[User] = None):
        self.room_id = room_id if room_id else str(uuid4())
        self.users = users if users else []

    async def broadcast(self, message: Optional[Dict, str]):
        async for user in self.users:
            await user.websocket.send_text(message)

    