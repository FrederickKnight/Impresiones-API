from ..models.models import (
    Base,
    
)
from sqlalchemy import (
    create_engine,
)

from sqlalchemy.orm import (
    sessionmaker
)

from dotenv import dotenv_values


def impresion_conn():
    
    db = dotenv_values(".env")["DB_NAME"]
    
    engine = create_engine(f'sqlite:///{db}')
    
    Base.metadata.create_all(engine)       

    Session = sessionmaker(bind=engine)
    session = Session()
    return session