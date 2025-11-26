from src.conexion.mySQL_queries import mySQL_queries

def main():
    print("🧹 Removendo banco de dados antigo...")

    db = mySQL_queries(can_write=True)
    conn = db.connect()
    cursor = conn.cursor()

    cursor.execute("DROP DATABASE IF EXISTS BIBLIOTECA;")
    cursor.execute("DROP DATABASE IF EXISTS biblioteca;")
    conn.commit()

    cursor.close()
    db.close()

    print("✅ Bancos 'BIBLIOTECA' e 'biblioteca' removidos com sucesso!")

if __name__ == "__main__":
    main()
