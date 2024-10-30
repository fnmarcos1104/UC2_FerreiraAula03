# BIBLIOTECAS: SQLALCHEMY, PYMYSQL


from sqlalchemy import create_engine, text

#VARIÁVEIS DE CONEXÃO COM O BANCO
host = 'localhost'
user = 'root'
password = 'root'
database = 'bd_produtos'

# FUNÇÃO PARA CONECTAR BANCO
def conecta_banco():
    try:
        #URL DE CONEXÃO COM O BANCO, USANDO SQLALCHEMY E PYMYSQL
        engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

        # ESTABELECE A CONEXÃO
        with engine.connect() as conexao:
            # QUERY: "Linguagem SQL para selecionar todos os registros da tabela produtos"
            query = "SELECT * FROM vendas"

            # 'text(query)' transforma a string da query em um objeto compatível com SQLAlchemy.
            # 'conexao.execute' executa essa consulta no banco de dados
            resultados = conexao.execute(text(query))

            for item in resultados:
                print(f'Produto: {item[0]}, Valor: {item[4]}, Quantidade : {item[5]}')


    except ImportError as e:
        print(f'Erro: {e}')

# CHAMA FUNÇÃO QUE CONECTA AO BANCO DE DADOS
conecta_banco()