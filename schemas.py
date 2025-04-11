
from pydantic import BaseModel

class PersonajeCreate(BaseModel):
    nombre: str
    nivel: int
    experiencia: int

class MisionCreate(BaseModel):
    titulo: str
    descripcion: str
    xp: int
