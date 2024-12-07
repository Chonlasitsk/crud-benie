from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
import os

from database.schemas import Person


async def init_database():
    client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))
    await init_beanie(database=client.practice_db, document_models=[Person])
    return client