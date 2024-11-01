from motor.motor_asyncio import AsyncIOMotorClient

# URL de conexão com o MongoDB
MONGO_URL = "mongodb://localhost:27017"

# Inicializar o cliente MongoDB e conectar ao banco de dados
client = AsyncIOMotorClient(MONGO_URL)
database = client['banco1']  # Nome do banco de dados
