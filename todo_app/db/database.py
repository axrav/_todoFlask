import os

import motor.motor_asyncio as mm

from config import DATABASE_URL as db_link

# client for mongodb motor
client = mm.AsyncIOMotorClient(db_link)

# choosing a database and collection
db = client["todo"]
todos = db["todos"]
