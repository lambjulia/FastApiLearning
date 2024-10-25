# crud.py
from bson import ObjectId
from database import mongo  # Importa a instância MongoDB

db = mongo.database

async def create_user(user_data):
    result = await db["users"].insert_one(user_data)
    user_data["id"] = str(result.inserted_id)
    return user_data

async def get_user(owner_id):
    user = await db["users"].find_one({"_id": ObjectId(owner_id)})
    return user

async def create_task(task_data):
    result = await db["tasks"].insert_one(task_data)
    task_data["id"] = str(result.inserted_id)
    return task_data

async def get_tasks(owner_id):
    tasks = []
    async for task in db["tasks"].find({"owner_id": owner_id}):
        tasks.append({"id": str(task["_id"]), **task})
    return tasks

async def update_task(task_id, task_data):
    await db["tasks"].update_one({"_id": ObjectId(task_id)}, {"$set": task_data})
    updated_task = await db["tasks"].find_one({"_id": ObjectId(task_id)})
    if updated_task:
        return {"id": str(updated_task["_id"]), **updated_task}
    return None

async def delete_task(task_id):
    result = await db["tasks"].delete_one({"_id": ObjectId(task_id)})
    return result.deleted_count > 0
