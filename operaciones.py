# Módulo de funciones puras (Paradigma Funcional)
from functools import reduce

def filtrar_pacientes_por_diagnostico(pacientes, palabra_clave):
    # filter: Aísla pacientes que coincidan con la búsqueda
    return list(filter(lambda p: palabra_clave.lower() in p.get_diagnostico().lower(), pacientes))

def obtener_nombres_pacientes(pacientes):
    # map: Extrae solo los nombres de una lista de pacientes
    return list(map(lambda p: p.get_nombre(), pacientes))

def contar_total_pacientes(pacientes):
    # reduce: Acumula el conteo total de pacientes
    return reduce(lambda acc, p: acc + 1, pacientes, 0)

def buscar_paciente_por_dni(pacientes, dni_buscado):
    # filter: Aísla al paciente que coincida exactamente con el DNI ingresado
    return list(filter(lambda p: p._dni == dni_buscado, pacientes))