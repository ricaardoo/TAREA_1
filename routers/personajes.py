
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter()

@router.post("/personajes")
def crear_personaje(personaje: schemas.PersonajeCreate, db: Session = Depends(get_db)):
    nuevo = models.Personaje(**personaje.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.get("/personajes/{personaje_id}")
def obtener_personaje(personaje_id: int, db: Session = Depends(get_db)):
    personaje = db.query(models.Personaje).filter(models.Personaje.id == personaje_id).first()
    return personaje
