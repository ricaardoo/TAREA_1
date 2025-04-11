
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Personaje(Base):
    __tablename__ = "personajes"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    nivel = Column(Integer)
    experiencia = Column(Integer)
    misiones = relationship("MisionPersonaje", back_populates="personaje")

class Mision(Base):
    __tablename__ = "misiones"
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    descripcion = Column(String)
    xp = Column(Integer)

class MisionPersonaje(Base):
    __tablename__ = "mision_personaje"
    id = Column(Integer, primary_key=True)
    personaje_id = Column(Integer, ForeignKey("personajes.id"))
    mision_id = Column(Integer, ForeignKey("misiones.id"))
    orden = Column(Integer)
    personaje = relationship("Personaje", back_populates="misiones")
    mision = relationship("Mision")
