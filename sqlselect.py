import pyodbc

#Dados de conexão
dados_conexao = (
    "Driver={SQL Server};"
    "Server=Nome do servidor;"
    "Database=Nome da base de dados;"
)


conexao = pyodbc.connect(dados_conexao)
print("Conexão bem sucedida")


cursor = conexao.cursor()


comando = "SELECT * FROM Acesso"


cursor.execute(comando)


for linha in cursor:
    print(linha)


conexao.close()
