from typing import (
    Optional
)

from sqlalchemy import (
    String,
    ForeignKey,
    Float,
    DateTime,
    Date,
    Boolean
)
from datetime import datetime,date

from sqlalchemy.orm import (
    declarative_base,
    Mapped,
    mapped_column
)

Base = declarative_base()


class Clientes(Base):
    __tablename__ = "cliente"
    
    id_cliente : Mapped[int] = mapped_column(primary_key=True)
    nombre : Mapped[str] = mapped_column(String(50))
    email : Mapped[Optional[str]] = mapped_column(String(50))
    numero : Mapped[str] = mapped_column(String(50))
    
    def __repr__(self) -> str:
        return f"<Cliente(id={self.id_cliente},nombre={self.nombre},email={self.email},numero={self.numero})>"
    
class Materiales(Base):
    __tablename__ = "material"
    
    id_material : Mapped[int] = mapped_column(primary_key=True)
    nombre : Mapped[str] = mapped_column(String(20))
    marca : Mapped[str] = mapped_column(String(20))
    medicion : Mapped[str] = mapped_column(String(5))
    color : Mapped[str] = mapped_column(String(30))
    
    def __repr__(self) -> str:
        return f"<Material(id={self.id_material},nombre={self.nombre},marca={self.marca},medicion={self.medicion},color={self.color})>"
    
class InventarioMaterial(Base):
    __tablename__ = "inventario_material"
    
    id_inventario: Mapped[int] = mapped_column(primary_key=True)
    id_material: Mapped[int] = mapped_column(ForeignKey("material.id_material"))
    cantidad: Mapped[Float] = mapped_column(Float)
    
    def __repr__(self) -> str:
        return f"<Inventario_Material(id={self.id_inventario},material={self.id_material},cantidad={self.cantidad})>"
    
class Inventario(Base):
    __tablename__ = "inventario"
    id_inventario: Mapped[int] = mapped_column(primary_key=True)
    tipo: Mapped[str] = mapped_column(String(50))
    nombre: Mapped[str] = mapped_column(String(50))
    descripcion: Mapped[str] = mapped_column(String(500))
    cantidad: Mapped[Float] = mapped_column(Float)
    medicion : Mapped[str] = mapped_column(String(5))
    
    def __repr__(self) -> str:
        return f"<Inventario(id={self.id_inventario},tipo={self.tipo},nombre={self.nombre},descripcion={self.descripcion},cantidad={self.cantidad},medicion={self.medicion})>"
    
class Tematicas(Base):
    __tablename__ = "tematica"
    
    id_tematica : Mapped[int] = mapped_column(primary_key=True)
    nombre : Mapped[str] = mapped_column(String(50))
    
    def __repr__(self) -> str:
        return f"<Tematica(id={self.id_tematica},nombre={self.nombre})>"
    
class Subtematica(Base):
    __tablename__ = "subtematica"
    
    id_subtematica: Mapped[int] = mapped_column(primary_key=True)
    id_tematica:Mapped[int]  = mapped_column(ForeignKey("tematica.id_tematica"))
    nombre : Mapped[str] = mapped_column(String(50))

    def __repr__(self) -> str:
        return f"<Subtematica(id={self.id_subtematica},tematica={self.id_tematica},nombre={self.nombre})>"

class Modelos(Base):
    __tablename__ = "modelo"
    
    id_modelo : Mapped[int] = mapped_column(primary_key=True)
    id_subtematica : Mapped[int]  = mapped_column(ForeignKey("subtematica.id_subtematica"))
    nombre : Mapped[str] = mapped_column(String(20))
    descripcion : Mapped[str] = mapped_column(String(500))
    direccion_archivo : Mapped[str] = mapped_column(String(200))
    
    def __repr__(self) -> str:
        return f"<Modelo(id={self.id_modelo},nombre={self.nombre},descripcion={self.descripcion},direccion_archivo={self.direccion_archivo})>"
    

class Costos_Generales(Base):
    __tablename__ = "costo_general"
    
    id_costo_general : Mapped[int] = mapped_column(primary_key=True)
    fecha : Mapped[date] = mapped_column(Date,default=datetime.now())
    id_material : Mapped[int] = mapped_column(ForeignKey("modelo.id_modelo"))
    desgaste : Mapped[Float] = mapped_column(Float)
    electricidad : Mapped[Float] = mapped_column(Float)
    riesgo_fallo_menor : Mapped[Float] = mapped_column(Float)
    riesgo_fallo_mediano : Mapped[Float] = mapped_column(Float)
    riesgo_fallo_mayor : Mapped[Float] = mapped_column(Float)
    margen : Mapped[Float] = mapped_column(Float)
    
    def __repr__(self) -> str:
        r = '<Costos_generales('
        r += f"id={self.id_costo_general},fecha={self.fecha},material={self.id_material},desgaste={self.desgaste},"
        r += f"electricidad={self.electricidad},riesgo_fallo_menor={self.riesgo_fallo_menor},"
        r += f"riesgo_fallo_mediano={self.riesgo_fallo_mediano},riesgo_fallo_mayor={self.riesgo_fallo_mayor},margen={self.margen}"
        return r

class Folios(Base):
    __tablename__ = "folio"
    
    id_folio : Mapped[int] = mapped_column(primary_key=True)
    folio : Mapped[str] = mapped_column(String(200))
    id_cliente : Mapped[int] = mapped_column(ForeignKey("cliente.id_cliente"))
    id_costo_general : Mapped[int] = mapped_column(ForeignKey("costo_general.id_costo_general"))
    fecha : Mapped[date] = mapped_column(Date,default=datetime.now())
    concepto : Mapped[String] = mapped_column(String(500))
    
    def __repr__(self) -> str:
        return f"<Folio(id={self.id_folio},folio={self.folio},cliente={self.id_cliente},costo_general={self.id_costo_general},fecha={self.fecha},concepto={self.concepto})>"
    
class ErrorFolio(Base):
    __tablename__ = "error_folio"
    
    id_error: Mapped[int] = mapped_column(primary_key=True)
    id_folio: Mapped[int] = mapped_column(ForeignKey("folio.id_folio"))
    id_modelo: Mapped[int] = mapped_column(ForeignKey("modelo.id_modelo"))
    merma: Mapped[Boolean] = mapped_column(Boolean)
    costo_reajustado: Mapped[Float] = mapped_column(Float)
    descripcion : Mapped[str] = mapped_column(String(500))
    
    def __repr__(self) -> str:
        return f"<Error_Folio(id={self.id_error},folio={self.id_folio},modelo={self.id_modelo},merma={self.merma},costo_reajustado={self.costo_reajustado},descripcion={self.descripcion})>"
    
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
        r += f"id={self.id_venta},folio={self.id_folio},modelo={self.id_modelo},material={self.id_material},"
        r += f"cantidad_material={self.cantidad_material},tiempo_impresion={self.tiempo_impresion},"
        f += f"costo_total={self.costo_total},descuento={self.descuento},costo_aplicado={self.costo_aplicado}"
        r += ")>"
        return r