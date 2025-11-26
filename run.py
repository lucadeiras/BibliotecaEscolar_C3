import subprocess
import sys

print("🚀 Iniciando o sistema da Biblioteca Escolar...\n")

# 1️⃣ Executa a criação das tabelas e inserção de dados
print("🧱 Etapa 1: Criando tabelas e registros iniciais...\n")
subprocess.run([sys.executable, "-m", "src.create_tables_and_records"])

# 2️⃣ Executa o sistema principal
print("\n🎬 Etapa 2: Iniciando o sistema principal...\n")
subprocess.run([sys.executable, "-m", "src.principal"])
