from fastapi import FastAPI
from database.database import database
from routers import user_router
from routers import task_router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    try:
        await database.command("ping")
        print("Conexão com o MongoDB bem-sucedida!")
    except Exception as e:
        print("Erro ao conectar ao MongoDB:", e)

@app.on_event("shutdown")
async def shutdown_db():
    await database.close_connection()

# Inclui as rotas das classes
app.include_router(user_router.router, prefix="/users", tags=["Users"])
app.include_router(task_router.router, prefix="/tasks", tags=["Tasks"])
