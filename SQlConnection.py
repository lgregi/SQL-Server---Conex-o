import pyodbc
dados_conexão = (
  "Driver={SQL Server};"
    "Server=Nome do servidor;"
   "Database=Nome da base de dados;"
)
#Variavel de conexão
conexao = pyodbc.connect(dados_conexão)
print("Conexao bem sucedida")
#variavel utilizada para executar comandos
cursor = conexao.cursor()


#comando SQL para inserir dados em uma tabela existente
comando = """INSERT INTO Acesso(id_acess,Nome,Email)
    VALUES ('1','Lucas','ls@gmail.com')"""
cursor.execute(comando)
cursor.commit()
