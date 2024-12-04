import time
import random

from sqlalchemy import text

from ..src.impresion_conn import impresion_conn

from ..models.models import (
    Folios
)


class FolioIdGenerador:
    def __init__(self):
        # Mantiene un registro de los IDs generados en esta instancia.
        self.generated_ids = set()
        self.sesion = impresion_conn()

    def generate_ticket_id(self):
        _temp = True
        while _temp:
            """Genera un ID único para un ticket."""
            timestamp = int(time.time())  # Tiempo en milisegundos
            random_part = random.randint(1000000000000, 99999999999999)  # Parte aleatoria
            ticket_id = f"{timestamp}{random_part}"
            folio = self.sesion.query(Folios).filter_by(folio = ticket_id).first()
            if folio == None:
                _temp = False
            return ticket_id
        

# Ejemplo de uso
if __name__ == "__main__":
    generator = FolioIdGenerador()
    for _ in range(5):  # Genera 5 IDs únicos
        generator.generate_ticket_id()
