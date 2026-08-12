# src/calendario.py
import os
import pandas as pd

def generar_calendario_mensual():
    print("=" * 60)
    print(" PANEL DE PLANIFICACIÓN EDITORIAL - GRUPO EMPRESARIAL HC ")
    print("=" * 60)
    
    # Definimos la parrilla de contenidos basada en nuestra estrategia mensual
    cronograma = [
        {"Semana": 1, "Día": "Lunes", "Pilar": "Educación / Dolor", "Formato": "Reel / Video Corto", "Tema": "¿Tienes más de 50 (mujeres) u 55 (hombres) y sigues pagando pensión obligatoria?"},
        {"Semana": 1, "Día": "Miércoles", "Pilar": "Mitos", "Formato": "Carrusel", "Tema": "Mito: Si dejo de cotizar pensión, pierdo todas las semanas acumuladas."},
        {"Semana": 1, "Día": "Viernes", "Pilar": "Caso de Éxito", "Formato": "Imagen / Testimonio", "Tema": "Aportes optimizados: Clientes que ya pagan solo EPS."},
        {"Semana": 2, "Día": "Lunes", "Pilar": "Educación / Dolor", "Formato": "Reel / Video Corto", "Tema": "¿Por qué los operadores de PILA rechazan el cambio sin asesoría experta?"},
        {"Semana": 2, "Día": "Miércoles", "Pilar": "Venta Suave", "Formato": "Post Educativo", "Tema": "El paso a paso de cómo te ayudamos en Grupo HC."},
        {"Semana": 2, "Día": "Viernes", "Pilar": "Mitos", "Formato": "Video Corto", "Tema": "¿Qué pasa con mi servicio de EPS si dejo de cotizar pensión?"},
        {"Semana": 3, "Día": "Lunes", "Pilar": "Educación / Dolor", "Formato": "Reel / Video Corto", "Tema": "Cuánto dinero real se ahorra un independiente al año dejando la pensión."},
        {"Semana": 3, "Día": "Miércoles", "Pilar": "Caso de Éxito", "Formato": "Captura WhatsApp", "Tema": "Lectura de mensajes felices de clientes asesorados."},
        {"Semana": 3, "Día": "Viernes", "Pilar": "Venta Directa", "Formato": "Post con CTA", "Tema": "Convocatoria abierta para revisión de casos esta semana al WhatsApp."},
        {"Semana": 4, "Día": "Lunes", "Pilar": "Mitos", "Formato": "Carrusel FAQ", "Tema": "Las 3 preguntas clave antes de pasar a pagar solo EPS."},
        {"Semana": 4, "Día": "Miércoles", "Pilar": "Educación / Legal", "Formato": "Video Explicativo", "Tema": "Lo que dice la norma en Colombia sobre la liberación de aportes."},
        {"Semana": 4, "Día": "Viernes", "Pilar": "Venta Directa", "Formato": "Reel de Cierre", "Tema": "Cierre de mes: No pagues de más. Escríbenos a WhatsApp."}
    ]
    
    # Convertimos la estructura a un DataFrame usando pandas
    df_calendario = pd.DataFrame(cronograma)
    
    # Mostramos un resumen en la terminal
    print(df_calendario.to_string(index=False))
    
    # Guardamos el calendario estructurado en la carpeta outputs (tanto en CSV como TXT)
    os.makedirs('outputs', exist_ok=True)
    df_calendario.to_csv('outputs/calendario_editorial_mes.csv', index=False, encoding='utf-8-sig')
    
    print("\n" + "=" * 60)
    print("[ÉXITO] Calendario editorial guardado en 'outputs/calendario_editorial_mes.csv'")
    print("=" * 60)

if __name__ == "__main__":
    generar_calendario_mensual()