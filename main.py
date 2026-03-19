import psycopg2
import os
import time

# Estas variables las llenaremos en Render
DB_URL = os.environ.get('DATABASE_URL')

print("Conectando a Supabase...")
try:
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute("SELECT nombre FROM usuarios;")
    records = cur.fetchall()
    
    print(f"He encontrado {len(records)} usuarios:")
    for row in records:
        print(f"- {row[0]}")
        
    cur.close()
    conn.close()
except Exception as e:
    print(f"Error: {e}")