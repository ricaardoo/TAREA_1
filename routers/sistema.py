
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.cola import MisionQueue
from app.models import MisionPersonaje

router = APIRouter()

@router.post("/personajes/{personaje_id}/misiones/{mision_id}")
def aceptar_mision(personaje_id: int, mision_id: int, db: Session = Depends(get_db)):
    cola = MisionQueue(db, personaje_id)
    cola.enqueue(mision_id)
    return {"mensaje": f"Misión {mision_id} asignada al personaje {personaje_id} exitosamente"}

@router.post("/personajes/{personaje_id}/completar")
def completar_mision(personaje_id: int, db: Session = Depends(get_db)):
    cola = MisionQueue(db, personaje_id)
    mision = cola.dequeue()
    return {"mensaje": f"Misión completada: {mision.mision_id}" if mision else "Sin misiones en cola"}

@router.get("/personajes/{personaje_id}/misiones")
def listar_misiones(personaje_id: int, db: Session = Depends(get_db)):
    misiones = (
        db.query(MisionPersonaje)
        .filter_by(personaje_id=personaje_id)
        .order_by(MisionPersonaje.orden.asc())
        .all()
    )
    return [{"mision_id": m.mision_id, "orden": m.orden} for m in misiones]
