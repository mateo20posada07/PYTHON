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

def lee_proyectos(ruta_fichero: str) -> list[Proyecto]:
    res = []
    with open (ruta_fichero, encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for id,titulo,categoria,fecha_inicio,fecha_fin,objetivo,recompensas in lector:
            id = id.strip()
            fecha_inicio = parsea_fecha (fecha_inicio)
            fecha_fin = parsea_fecha (fecha_fin)
            objetivo = float(objetivo)
            recompensas = parsea_recompensas(id[:2], recompensas)
            res.append(Proyecto(id, titulo, categoria, fecha_inicio, fecha_fin, \
            objetivo, recompensas))
    return res
def parsea_fecha(fecha_str: str) -> date:
    return datetime.strptime(fecha_str, "%Y-%m-%d").date()
def parsea_recompensas (origen: str, recompensas_str: str) -> list[Recompensa]:
    res = []
    origen = origen.upper()
    separador = obtener_separador(origen)
    trozos = recompensas_str.split(separador)
    for trozo in trozos:
        if origen == "KS":
            recompensa = parsear_recompensa_ks(trozo)
        elif origen == "CF":
            recompensa = parsear_recompensa_cf(trozo)
        if recompensa:
         res.append(recompensa)
    return res
def obtener_separador (origen: str) -> str:
    separador = ""
    if origen == "KS":
        separador =";"
    elif origen == "CF":
        separador ="|"
    return separador
def parsear_recompensa_ks(recompesa_str: str) -> Recompensa:
    separador = ":"
    importe, patrocinadores, nombre = recompesa_str.split(separador)
    return Recompensa(nombre, float(importe), int(patrocinadores))
def parsear_recompensa_cf(recompesa_str: str) -> Recompensa:
    separador = "@"
    nombre, importe, patrocinadores = recompesa_str.split(separador)
    return Recompensa(nombre, float(importe), int(patrocinadores))

