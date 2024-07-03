import os
from sqlalchemy import create_engine # representar motor de base de datos trabajado
from sqlalchemy.orm.session import sessionmaker # abrir sesión para hacer operaciones
from sqlalchemy.ext.declarative import declarative_base

# nombre de la base de datos a nivel main
sqlite_file_name = "../database.sqlite" 
# Leer directorio actual que es database.py
base_dir = os.path.dirname(os.path.realpath(__file__))

# Crear url de base de datos unida con las dos variables anteriores
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

engine = create_engine(database_url, echo=True)
Session = sessionmaker(bind = engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base() # maneja las tablas