
from sqlalchemy.orm import Session
from .models import MisionPersonaje

class MisionQueue:
    MisionPersonaje = MisionPersonaje

    def __init__(self, db: Session, personaje_id: int):
        self.db = db
        self.personaje_id = personaje_id

    def enqueue(self, mision_id: int):
        ultima = (
            self.db.query(MisionPersonaje)
            .filter(MisionPersonaje.personaje_id == self.personaje_id)
            .order_by(MisionPersonaje.orden.desc())
            .first()
        )
        nuevo_orden = 0 if not ultima else ultima.orden + 1
        nueva = MisionPersonaje(
            personaje_id=self.personaje_id,
            mision_id=mision_id,
            orden=nuevo_orden
        )
        self.db.add(nueva)
        self.db.commit()

    def dequeue(self):
        primera = (
            self.db.query(MisionPersonaje)
            .filter(MisionPersonaje.personaje_id == self.personaje_id)
            .order_by(MisionPersonaje.orden.asc())
            .first()
        )
        if primera:
            self.db.delete(primera)
            self.db.commit()
            return primera
        return None
