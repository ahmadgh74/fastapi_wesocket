from fastapi import WebSocket


class User:

    def __init__(self, websocket: WebSocket, user_id: str = None, name: str = None):
        self.websocket = websocket
        self.user_id = user_id
        self.name = name

    async def send_to(self, message: str):
        await self.websocket.send_text(message)
