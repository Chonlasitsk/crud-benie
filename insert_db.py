from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from bson.json_util import loads, CANONICAL_JSON_OPTIONS
import asyncio
import os
import json

from database.schemas import Person, Address, PhoneNumber
from database.init_db import init_database

async def inserting_to_db():
    client = await init_database()

    # insert from json file 
    with open("example_person.json", "r", encoding="utf-8") as file:
        sample_data_obj = json.loads(file.read())
    
    # use beanie insert
    # persons = []
    # for data in sample_data_obj:
    #     address = Address(**data["address"])
    #     phone_numbers = [PhoneNumber(**phone_data) for phone_data in data["phone_numbers"]]
    #     data_exclude = {k: v for k, v in data.items() if k not in  ["address", "phone_numbers"]}
    #     person = Person(**data_exclude, address=address, phone_number=phone_numbers)
    #     persons.append(person)

    # await Person.insert_many(documents=persons)

    # use motor insert many
    await client.practice_db.persons.insert_many(documents=sample_data_obj)

if __name__ == "__main__":
    asyncio.run(inserting_to_db())
    