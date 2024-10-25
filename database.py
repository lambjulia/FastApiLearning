import motor.motor_asyncio
import os

class MongoDB:
    def __init__(self, uri: str, db_name: str):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(uri)
        self.database = self.client[db_name]

    async def close(self):
        self.client.close()

# Construa a URI de conexão
MONGO_URI = f"mongodb+srv://reversejulia:Justin0103@teste.ppfsu.mongodb.net/teste?retryWrites=true&w=majority"

mongo = MongoDB(MONGO_URI, "teste")  # Inicialize a conexão com o banco de dados

