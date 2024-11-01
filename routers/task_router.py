from fastapi import APIRouter, HTTPException
from models.model_task import Task
from logics.task_logic import TaskLogic

router = APIRouter()

class RouterV1Task:

    def __init__(self):
        pass

    @router.get("/", response_model=list[Task])
    async def read_tasks(owner_id: str):
        success = await TaskLogic().get_tasks(owner_id)
        if not success:
            raise HTTPException(status_code=404, detail="Task not found")
        return success

    @router.post("/", response_model=Task)
    async def create_task_endpoint(task: Task):
        task_data = task.dict(by_alias=True)  # Converte o modelo para dicionário
        created_task = await TaskLogic().create_task(task_data)  # Chama o método na instância
        return created_task

    @router.put("/{task_id}", response_model=Task)
    async def update_task_endpoint(task_id: str, task: Task):
        updated_task = await TaskLogic().update_task(task_id, task.dict(exclude_unset=True))  # Usando dicionário
        if updated_task:
            return updated_task
        raise HTTPException(status_code=404, detail="Task not found")

    @router.delete("/{task_id}")
    async def delete_task_endpoint(task_id: str):
        success = await TaskLogic().delete_task(task_id)
        if not success:
            raise HTTPException(status_code=404, detail="Task not found")
        return {"message": "Task deleted successfully"}

