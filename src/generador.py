# src/generador.py
import sys
import os

# Agregamos la ruta raíz para importar la base de datos
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.normativa_colombia import BASE_CONOCIMIENTO_HC

def generar_contenido_automatico():
    print("=" * 60)
    print(" DEPARTAMENTO DE MARKETING Y LEGAL - GRUPO EMPRESARIAL HC ")
    print("=" * 60)
    
    norma = BASE_CONOCIMIENTO_HC["normas_clave"][0]
    dolor = BASE_CONOCIMIENTO_HC["dolores_usuario"][0]
    cta = BASE_CONOCIMIENTO_HC["llamados_accion"][0]
    
    print(f"\n[NORMA APLICADA]: {norma['tema']}")
    print(f"Descripción legal: {norma['descripcion']}")
    print(f"Impacto financiero: {norma['beneficio_financiero']}")
    
    print("\n" + "-" * 60)
    print(" PROPUESTA DE CONTENIDO AUTOMATIZADA PARA HOY ")
    print("-" * 60)
    
    copy_redes = f"""
    🛑 ¿Te identificas con esto? '{dolor}'
    
    En Colombia, la ley establece que {norma['descripcion'].lower()}
    
    {cta}
    """
    print(copy_redes.strip())
    
    # Guardamos el resultado en la carpeta outputs
    os.makedirs('outputs', exist_ok=True)
    with open('outputs/contenido_generado.txt', 'w', encoding='utf-8') as f:
        f.write(copy_redes)
    
    print("\n[ÉXITO] Contenido generado y guardado en 'outputs/contenido_generado.txt'")

if __name__ == "__main__":
    generar_contenido_automatico()