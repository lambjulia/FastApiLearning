# main.py
from fastapi import FastAPI, HTTPException
from models import User, Task
from crud import create_user, get_user, create_task, get_tasks, update_task, delete_task
from database import mongo

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    try:
        # Tenta fazer uma operação simples no banco de dados
        await mongo.database.command("ping")  # Use mongo.database em vez de db
        print("Conexão com o MongoDB bem-sucedida!")
    except Exception as e:
        print("Erro ao conectar ao MongoDB:", e)


@app.on_event("shutdown")
async def shutdown_db():
    await mongo.close()

@app.post("/users/", response_model=User)
async def register_user(user: User):
    user_data = user.dict(by_alias=True)
    created_user = await create_user(user_data)
    return created_user

@app.get("/tasks/", response_model=list[Task])
async def read_tasks(owner_id: str):
    return await get_tasks(owner_id)

@app.post("/tasks/", response_model=Task)
async def create_task_endpoint(task: Task):
    task_data = task.dict(by_alias=True)
    created_task = await create_task(task_data)
    return created_task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task_endpoint(task_id: str, task: Task):
    task_data = task.dict(exclude_unset=True, by_alias=True)
    updated_task = await update_task(task_id, task_data)
    if updated_task:
        return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
async def delete_task_endpoint(task_id: str):
    success = await delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
