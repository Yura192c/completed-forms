from motor.motor_asyncio import AsyncIOMotorClient

from config.settings import settings_db as config

async_client = AsyncIOMotorClient(config.database_url)

try:
    async_db = async_client[config.MONGODB_NAME]
    async_collection = async_db[config.MONGODB_COLLECTION]
except Exception as e:
    print("Connection to database error")
    print(e)
