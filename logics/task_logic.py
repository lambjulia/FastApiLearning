from bson import ObjectId
from database.database import database  # Importa a instância do banco de dados

class TaskLogic:
    def __init__(self):
        self.collection = database["tasks"]

    async def create_task(self, task_data: dict):
        # Insere a tarefa no banco e converte o ID para string
        result = await self.collection.insert_one(task_data)
        task_data["id"] = str(result.inserted_id)
        return task_data

    async def get_tasks(self, owner_id: str):
        tasks = []
        # Busca as tarefas com o owner_id e converte cada _id para id
        async for task in self.collection.find({"owner_id": owner_id}):
            task["id"] = str(task.pop("_id"))
            tasks.append(task)
        return tasks

    async def update_task(self, task_id: str, task_data: dict):
        # Converte o task_id para ObjectId e atualiza a tarefa
        await self.collection.update_one({"_id": ObjectId(task_id)}, {"$set": task_data})
        updated_task = await self.collection.find_one({"_id": ObjectId(task_id)})
        if updated_task:
            updated_task["id"] = str(updated_task.pop("_id"))
            return updated_task
        return None

    async def delete_task(self, task_id: str):
        # Deleta a tarefa e retorna True se a contagem de deletados for maior que 0
        result = await self.collection.delete_one({"_id": ObjectId(task_id)})
        return result.deleted_count > 0
