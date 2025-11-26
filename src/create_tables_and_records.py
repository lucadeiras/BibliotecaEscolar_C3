import os
from pathlib import Path
import mysql.connector
from src.conexion.mySQL_queries import mySQL_queries

def executar_sql(conn, caminho_arquivo):
    """Executa os comandos SQL contidos em um arquivo."""
    try:
        cursor = conn.cursor()
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            script = f.read()

            # Divide os comandos de forma segura (ignora linhas em branco)
            comandos = [cmd.strip() for cmd in script.split(';') if cmd.strip()]

            for comando in comandos:
                try:
                    cursor.execute(comando)
                except mysql.connector.Error as e:
                    # Ignora erros de duplicação, mas mostra aviso
                    if e.errno == 1062:  # Duplicate entry
                        print(f"⚠️  Aviso: registro duplicado em {caminho_arquivo.name} → {e.msg}")
                    elif e.errno == 1050:  # Table already exists
                        print(f"ℹ️  Tabela já existente em {caminho_arquivo.name} → {e.msg}")
                    else:
                        print(f"❌ Erro ao executar comando em {caminho_arquivo.name}: {e.msg}")
        conn.commit()
        cursor.close()
        print(f"✅ Arquivo {caminho_arquivo.name} executado com sucesso.\n")

    except Exception as e:
        print(f"❌ Erro ao executar {caminho_arquivo.name}: {e}\n")


def main():
    print("🚀 Iniciando configuração do banco de dados da Biblioteca Escolar...\n")

    # 🔹 Conecta ao servidor MySQL (sem selecionar banco ainda)
    try:
        conn = mysql.connector.connect(
            host="mysql-c2-lucasdavi22-6e55.k.aivencloud.com",
            port=19016,
            user="avnadmin",
            password="AVNS_SuIzlyyt0jsgcBnycgi"
        )
        print("🟢 Conexão inicial com o servidor MySQL Aiven estabelecida com sucesso.")
    except Exception as e:
        print(f"🚨 Erro de conexão com o MySQL Aiven: {e}")
        return

    try:
        cursor = conn.cursor()

        # 🔹 Cria e usa o banco (caso não exista)
        cursor.execute("CREATE DATABASE IF NOT EXISTS biblioteca;")
        cursor.execute("USE biblioteca;")
        print("🏗️ Banco de dados 'biblioteca' criado/selecionado com sucesso.\n")

        # 🔹 Caminho para a pasta /sql
        base_path = Path(__file__).resolve().parent.parent / "sql"

        sql_files = [
            base_path / "01_Create_Tables_Biblioteca.sql",
            base_path / "02_Insert_Core_Data.sql",
            base_path / "03_Insert_Related_Data.sql"
        ]

        print("📚 Etapa 1: Criando tabelas e inserindo registros iniciais...\n")

        for sql_file in sql_files:
            if sql_file.exists():
                print(f"📄 Executando: {sql_file}")
                executar_sql(conn, sql_file)
            else:
                print(f"⚠️ Arquivo SQL não encontrado: {sql_file.name} (pulando)\n")

        print("✅ Etapa concluída com sucesso! Todas as tabelas e registros foram processados.\n")

    except Exception as e:
        print(f"❌ Erro geral durante o processo: {e}")

    finally:
        conn.close()
        print("🔒 Conexão com o MySQL encerrada.\n")


if __name__ == "__main__":
    main()
