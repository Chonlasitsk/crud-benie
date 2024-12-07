from database.schemas import Person, PersonView
import asyncio

from database.init_db import init_database

async def update_document():
    await init_database()

     # use "save()" instance method to update 
    book_to_update = await Person.find_one("<condition>")
    book_to_update.title = "like something forever 2"
    book_to_update.price = 8500
    await book_to_update.save()

