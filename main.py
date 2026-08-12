# main.py
import sys
import os

# Agregamos la ruta src al path para poder importar nuestros módulos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from generador import generar_contenido_automatico
from calendario import generar_calendario_mensual

def ejecutar_sistema_hc():
    print("*" * 70)
    print(" INICIANDO SISTEMA AUTOMATIZADO DE MARKETING Y LEGAL - GRUPO HC ")
    print("*" * 70)
    
    # 1. Ejecutamos la generación del contenido del día
    print("\n[PASO 1/2] Ejecutando motor de contenidos y normativa...")
    generar_contenido_automatico()
    
    print("\n" + "=" * 70)
    
    # 2. Ejecutamos el planificador del calendario mensual
    print("\n[PASO 2/2] Actualizando panel de planificación editorial...")
    generar_calendario_mensual()
    
    print("\n" + "*" * 70)
    print(" ¡PROCESO FINALIZADO CON ÉXITO! Revisa la carpeta 'outputs/'. ")
    print("*" * 70)

if __name__ == "__main__":
    ejecutar_sistema_hc()