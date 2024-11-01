from bson import ObjectId
from database.database import database  # Importa a instância do banco de dados

class UserLogic:
    def __init__(self):
        self.collection = database["users"]

    async def create_user(user_data: dict):
        result = await database["users"].insert_one(user_data)
        user_data["id"] = str(result.inserted_id)
        return user_data

    async def get_user(self, owner_id: str):
        try:
            # Converte o owner_id para ObjectId antes da consulta
            user = await self.collection.find_one({"_id": ObjectId(owner_id)})
            if user:
                # Converte o _id para string e o renomeia para id
                user["id"] = str(user.pop("_id"))
            return user
        except Exception as e:
            print(f"Erro ao buscar usuário: {e}")
            return None
