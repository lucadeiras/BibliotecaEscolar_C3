import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host= "biblioteca-mysql-aiven-lab.aivencloud.com",  # ou o host que vocês usam
        port= 19016,  # coloca aqui a porta do banco
        database= "biblioteca",  # nome do banco
        user= "avnadmin",  # teu usuário MySQL
        password= "AVNS_SuIzlyyt0jsgcBnycgi"  # tua senha MySQL
    )

    if connection.is_connected():
        print("✅ Conexão com MySQL estabelecida com sucesso!")
        db_info = connection.get_server_info()
        print("Versão do servidor MySQL:", db_info)

except Error as e:
    print("❌ Erro ao conectar ao MySQL:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("🔒 Conexão com MySQL fechada.")
