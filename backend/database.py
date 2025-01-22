import os 
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import asyncio

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL","mongodb://localhost:27017")

client = AsyncIOMotorClient(MONGO_URL)
db = client["iyte_place_db"]

pixels_collection = db["pixels"]

async def create_indexes():
    await pixels_collection.create_index([("x",1),("y",1)],unique=True)


#if __name__ == "__main__":
#    asyncio.run(create_indexes())
