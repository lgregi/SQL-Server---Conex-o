import pyodbc

# conexão com o banco de dados
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=(local)\SQLEXPRESS;'
                      'AttachDbFileName=C:\Caminho\para\seu\arquivo.mdf;'
                      'Database=NomeDoBancoDeDados;'
                      'Trusted_Connection=yes;')


cursor = conn.cursor()


cursor.execute('SELECT * FROM NomeDaTabela')


for row in cursor:
    print(row)


conn.close()
