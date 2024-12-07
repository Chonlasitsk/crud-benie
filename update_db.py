from database.schemas import Person, PersonView
import asyncio

from database.init_db import init_database

async def update_document():
    await init_database()

     # use "save()" instance method to update 
    person_to_update = await Person.find_one(Person.first_name == "John")
    person_to_update.age = 100
    await person_to_update.save()

if __name__ == "__main__":
    asyncio.run(update_document())
