from typing import (
    List,
    Optional
)

from sqlalchemy import (
    String,
    ForeignKey,
    Float,
    create_engine
)

from sqlalchemy.orm import (
    declarative_base,
    Mapped,
    mapped_column,
    relationship,
    sessionmaker
)

Base = declarative_base()


class Clientes(Base):
    __tablename__ = "cliente"
    
    id_cliente : Mapped[int] = mapped_column(primary_key=True)
    nombre : Mapped[str] = mapped_column(String(50))
    email : Mapped[Optional[str]]
    numero : Mapped[str] = mapped_column(String(15))
    
    def __repr__(self) -> str:
        return f"<Cliente(id={self.id_cliente}, nombre={self.nombre}, email={self.email}, numero={self.numero})>"
    
class Materiales(Base):
    __tablename__ = "material"
    
    id_material : Mapped[int] = mapped_column(primary_key=True)
    nombre : Mapped[str] = mapped_column(String(20))
    marca : Mapped[str] = mapped_column(String(20))
    medicion : Mapped[str] = mapped_column(String(20))
    color : Mapped[str] = mapped_column(String(30))
    
    def __repr__(self) -> str:
        return f"<Material(id={self.id_material}, nombre={self.nombre},marca={self.marca},medicion={self.medicion})>"
    
class Tematicas(Base):
    __tablename__ = "tematica"
    
    id_tematica : Mapped[int] = mapped_column(primary_key=True)
    nombre : Mapped[str] = mapped_column(String(50))
    
    def __repr__(self) -> str:
        return f"<Tematica(id={self.id_tematica},nombre={self.nombre})>"

class Modelos(Base):
    __tablename__ = "modelo"
    
    id_modelo : Mapped[int] = mapped_column(primary_key=True)
    nombre : Mapped[str] = mapped_column(String(20))
    id_tematica : Mapped[str]  = mapped_column(ForeignKey("tematica.id_tematica"))
    descripcion : Mapped[str] = mapped_column(String(500))
    direccion_archivo : Mapped[str] = mapped_column(String(200))
    
    def __repr__(self) -> str:
        return f"<Modelo(id={self.id_modelo},nombre={self.nombre},descripcion={self.descripcion},direccion={self.direccion_archivo})>"
    

class Costos_Generales(Base):
    __tablename__ = "costo_general"
    
    id_costo_general : Mapped[int] = mapped_column(primary_key=True)
    fecha : Mapped[str] = mapped_column(String(12))
    id_material : Mapped[int] = mapped_column(ForeignKey("modelo.id_modelo"))
    desgaste : Mapped[Float] = mapped_column(Float)
    electricidad : Mapped[Float] = mapped_column(Float)
    riesgo_fallo_menor : Mapped[Float] = mapped_column(Float)
    riesgo_fallo_mediano : Mapped[Float] = mapped_column(Float)
    riesgo_fallo_mayor : Mapped[Float] = mapped_column(Float)
    margen : Mapped[Float] = mapped_column(Float)
    
    def __repr__(self) -> str:
        r = '<Costos_generales('
        r += f"id={self.id_costo_general},fecha={self.fecha},material={self.id_material},desgaste={self.desgaste}"
        r += f"electricidad={self.electricidad},riesgo_fallo_menor={self.riesgo_fallo_menor},"
        r += f"riesgo_fallo_mediano={self.riesgo_fallo_mediano},riesgo_fallo_mayor={self.riesgo_fallo_mayor},margen={self.margen}"
        return r

class Folios(Base):
    __tablename__ = "folio"
    
    id_folio : Mapped[int] = mapped_column(primary_key=True)
    folio : Mapped[str] = mapped_column(String(200))
    id_cliente : Mapped[int] = mapped_column(ForeignKey("cliente.id_cliente"))
    id_costo_general : Mapped[int] = mapped_column(ForeignKey("costo_general.id_costo_general"))
    fecha : Mapped[str] = mapped_column(String(12))
    concepto : Mapped[String] = mapped_column(String(500))
    
    def __repr__(self) -> str:
        return f"<Folio(id={self.id_folio},cliente={self.id_cliente},costo_general={self.id_costo_general},fecha={self.fecha},concepto={self.concepto})>"
    
    
class Ventas(Base):
    __tablename__ = "venta"
    
    id_venta : Mapped[int] = mapped_column(primary_key=True)
    id_folio : Mapped[int] = mapped_column(ForeignKey("folio.id_folio"))
    id_modelo : Mapped[int] = mapped_column(ForeignKey("modelo.id_modelo"))
    id_material : Mapped[int] = mapped_column(ForeignKey("material.id_material"))
    cantidad_material : Mapped[Float] = mapped_column(Float)
    tiempo_impresion : Mapped[Float] = mapped_column(Float)
    costo_total : Mapped[Float] = mapped_column(Float)
    descuento : Mapped[Float] = mapped_column(Float)
    costo_aplicado : Mapped[Float] = mapped_column(Float)
    
    def __repr__(self) -> str:
        r = "<Ventas("
        r += f"id={self.id_venta},folio={self.id_folio},modelo={self.id_modelo},material={self.id_material}"
        r += ")>"
        # r = f"<Ventas(id={self.id_venta},folio={self.id_folio},modelo={self.id_modelo},material={self.id_material},cantidad_material={self.cantidad_material},tiempo_impresion={self.cantidad_material},costo_total={self.costo_total},descuento={self.descuento},costo_aplicado={self.costo_aplicado})>"
        return r