from src.conexion.mySQL_queries import mySQL_queries

# Inicializa conexão com permissão de escrita
mysql = MySQLQueries(can_write=True)

# Conecta ao banco MySQL (configuração vem do arquivo src/utils/config.py)
mysql.connect()


# Teste de SELECT simples
result = mysql.sqlToMatrix("SELECT NOW();")
print("Resultado (Matrix):")
print(result)

print()


result = mysql.sqlToDataFrame("SELECT NOW();")
print("Resultado (DataFrame):")
print(result)

print()

result = mysql.sqlToJson("SELECT NOW();")
print("Resultado (JSON):")
print(result)
print()

# Teste de DDL + INSERT + SELECT + DROP
mysql.executeDDL("CREATE TABLE test_float (x DECIMAL(5, 3));")

mysql.write("INSERT INTO test_float VALUES (7.1);")
mysql.write("INSERT INTO test_float VALUES (8.4);")

result = mysql.sqlToDataFrame("SELECT * FROM test_float;")
print("Conteúdo da tabela test_float:")
print(result)
print()

mysql.executeDDL("DROP TABLE test_float;")
print("Tabela test_float removida com sucesso.")
