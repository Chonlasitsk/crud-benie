from database.schemas import Person, PersonView
import asyncio

from database.init_db import init_database
async def find_document():
   
   await init_database()
    # finding multiple documents in the database is to call "find()" class method with some search critiria (like WHERE in SQL)
   res_documents = await Person.find().to_list()
   document = res_documents[0]
   document_dict = document.model_dump()
   print(document_dict["first_name"])

     # finding multiple documents in the database with conditions
   res_document = await Person.find(Person.price > 300).to_list()

   # finding multiple documents in the database with conditions and projection (like SELECT command in SQL)
   res_document = await Person.find(Person.price > 300).project(PersonView).to_list()
   res_document = await Person.find(Person.title == "The lord of the ring").project(PersonView).to_list()
   
   # Other MongoDB query operator can be used from "beanie.operators"
   from beanie.operators import In
   res_document = await Person.find(In(Person.title, ["The last of us", "Sometime"])).to_list()

   # finding mulitple documents more than conditions 
   res_document = await Person.find(Person.title == "King landing 1", Person.price > 200).to_list()

   # Sorting, you can sorting by call "sort()" method 
   # Pass it one or multiple fields to sort by. You may optionally specify a + or - (denoting ascending and descending respectively).
   res_document = await Person.find().sort(-Person.price).to_list()

   # Skip and limit
   res_document = await Person.find().limit(2).to_list()
   res_document = await Person.find().skip(3).to_list()



if __name__ == "__main__":
   asyncio.run(find_document())
