import httpx
from utils.singleton import Singleton
# import asyncio


class NotificationRequests(metaclass=Singleton):
    SEND_EMAIL_URL = 'http://localhost:8001/api/notification/send_email'

    async def register(self, data: dict):
        response = await self.apost(self.REGISTER_URL, data)
        return response

    async def apost(self, url: str, data: dict):
        async with httpx.AsyncClient() as client:
            return await client.post(url=url, json=data)
        

