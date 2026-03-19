import psycopg2
import os

# Esto nos dirá si la variable llegó o no
DATABASE_URL = os.environ.get('DATABASE_URL')

if not DATABASE_URL:
    print("ERROR: No se encontró la variable DATABASE_URL. Revisa la configuración en la nube.")
else:
    print(f"Variable detectada correctamente (empieza con: {DATABASE_URL[:15]}...)")

def conectar_y_leer():
    # ... el resto de tu código sigue igual ...
