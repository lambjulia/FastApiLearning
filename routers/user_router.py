from fastapi import APIRouter
from models.model_user import User
from logics.user_logic import UserLogic

router = APIRouter()

class RouterV1User:

    def __init__(self):
        pass

    @router.post("/", response_model=User)
    async def register_user(user: User):
            # Convertendo o modelo para dicionário
            user_data = user.dict(by_alias=True)
            created_user = await UserLogic.create_user(user_data)
            return created_user