
from fastapi import FastAPI
from app.routers import personajes, misiones, sistema
from app.database import Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(personajes.router)
app.include_router(misiones.router)
app.include_router(sistema.router)
