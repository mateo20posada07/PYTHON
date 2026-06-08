# En cada línea del archivo se recoge la siguiente información sobre cada proyecto,
# consistente con el NamedTuple que se facilita más adelante: 
# • Identificador del proyecto (cadena: 'CF' o 'KS' seguido de número) 
# • Título del proyecto 
# • Categoría 
# • Fecha de inicio de la campaña 
# • Fecha de fin de la campaña 
# • Objetivo de financiación (float) 
# • Listado de recompensas disponibles 

# Proyectos CF (CrowdFund): 
# Las recompensas están separadas por '|' (barra vertical). Cada recompensa 
# contiene tres datos separados por '@': nombre, importe por unidad y 
# número de patrocinadores. 
# Ejemplo: Early Bird@89.0@150|Estándar@129.0@320 
# Proyectos KS (KickStarter): 
# Las recompensas están separadas por ';' (punto y coma). Cada recompensa contiene 
# tres datos separados por ':' (dos puntos) en el orden: importe por unidad, 
# número de patrocinadores y nombre. 
# Ejemplo: 89.0:150:Early Bird;129.0:320:Estándar
from typing import NamedTuple, List,Tuple
from datetime import *
import csv

Recompensa = NamedTuple("Recompensa", [ 
("nombre", str), 
("importe", float), 
("patrocinadores", int) 
]) 
Proyecto = NamedTuple("Proyecto", [ 
("id", str), 
("titulo", str), 
("categoria", str), 
("fecha_inicio", date), 
("fecha_fin", date), 
("objetivo", float), 
("recompensas", list[Recompensa]) 
]) 

def lee_crowdfunding(fichero: str)->List[Proyecto]:
    res=list()
    with open(fichero, encoding='utf-8') as f:
    lector=csv.reader(f)
    next(lector)
    for id, titulo, categoria, fechaInicio, fechaFin,objetivo, recompensas in lector:
    
        fechaInicio= date


