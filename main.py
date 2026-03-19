import psycopg2
import os
import sys

# 1. Intentar leer la variable de entorno
DATABASE_URL = os.environ.get('DATABASE_URL')

def conectar_y_leer():
    # Revisamos si la variable existe antes de intentar conectar
    if not DATABASE_URL:
        print("ERROR: No se encontró la variable DATABASE_URL en el sistema.")
        return

    try:
        print("Conectando a Supabase...")
        # 2. Establecer la conexión
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        
        # 3. Ejecutar la consulta
        print("Consultando nombres en la tabla Usuarios...")
        cur.execute("SELECT nombre FROM Usuarios;")
        
        # 4. Obtener y mostrar resultados
        rows = cur.fetchall()
        print(f"--- Se encontraron {len(rows)} registros ---")
        for row in rows:
            print(f"Usuario: {row[0]}")
            
        cur.close()
        conn.close()
        print("Proceso finalizado con éxito.")

    except Exception as e:
        print(f"¡Oops! Algo salió mal durante la ejecución: {e}")

if __name__ == "__main__":
    conectar_y_leer()
