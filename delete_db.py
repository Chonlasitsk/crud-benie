from database.schemas import Person, PersonView
import asyncio

from database.init_db import init_database

async def delete_document():
    await init_database()

    person_to_delete = await Person.find_one(Person.first_name == "John")
    await person_to_delete.delete()

if __name__ == "__main__":
    asyncio.run(delete_document())
