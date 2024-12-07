from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from database.schemas import Person, Stock


async def init_database():
    client = AsyncIOMotorClient("mongodb://root:root@localhost:27019/")
    await init_beanie(database=client.practice_db, document_models=[Person, Stock])
    return client