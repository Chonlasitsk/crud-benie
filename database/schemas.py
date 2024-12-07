from typing import Optional, List
from pydantic import BaseModel, EmailStr
from beanie import Document

"""
{
  "_id": "64b0c63ef3a7f4b1a5c89b7a",
  "first_name": "John",
  "last_name": "Doe",
  "age": 29,
  "email": "john.doe@example.com",
  "address": {
    "street": "123 Elm St",
    "city": "Metropolis",
    "state": "NY",
    "zip": "10001",
    "country": "USA"
  },
  "phone_numbers": [
    {
      "type": "home",
      "number": "555-123-4567"
    },
    {
      "type": "work",
      "number": "555-987-6543"
    }
  ],
  "tags": ["developer", "python", "mongodb"]
}

"""

class PhoneNumber(BaseModel):
    type: str
    number: str

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip: str
    country: str

class Person(Document):
    first_name: Optional[str]
    last_name: Optional[str]
    age: Optional[int]
    email: Optional[EmailStr]
    address: Optional[Address]
    phone_numbers: Optional[List[PhoneNumber]]
    tags: Optional[List[str]]

    class Settings:
        name = "persons"

    
class PersonView(BaseModel):
    first_name: str
    last_name: str
    age: int
    
    
class Stock(Document):
    name: str
    price: int
    class Settings:
        name = "stocks"