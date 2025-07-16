#0 fazer a conexao com o MYSQL
#1º Solicitar ao usuario a quantidade de arquivo que deseja
#2º Solicitar o local de cada arquivo
#3º Inserir os dados em um dicionario
#3º Ler o arquivo e transformar ele para os inserts conforme SQL
import csv

qtd_arquivo=int(input('Quantos arquivos quer fazer upload? '))
lista_filmes=[]

def ler_csv():
    for i in range(qtd_arquivo):
        caminho_arquivo=input('Digite o caminho do arquivo: ')
        with open(caminho_arquivo, 'r') as arq:
            ler_linha = arq.readlines()
            linhas_corrigidas = [linha.replace(';', ',') for linha in ler_linha]
            lista_filmes.append(linhas_corrigidas)
    return lista_filmes

def criar_tabelas(cursor):
    comandos = [
        """
        CREATE TABLE IF NOT EXISTS movies (
            id_filme INT AUTO_INCREMENT PRIMARY KEY,
            nome_filme VARCHAR(150) NOT NULL,
            ano_filme INT NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS categorias (
            id_categoria INT AUTO_INCREMENT PRIMARY KEY,
            nome_categoria VARCHAR(100) NOT NULL UNIQUE,
            descricao TEXT
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS filme_categoria (
            id_filme INT NOT NULL,
            id_categoria INT NOT NULL,
            PRIMARY KEY (id_filme, id_categoria),
            FOREIGN KEY (id_filme) REFERENCES movies(id_filme)
                ON UPDATE CASCADE
                ON DELETE CASCADE,
            FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
                ON UPDATE CASCADE
                ON DELETE RESTRICT
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS filmes_imdb (
            id_filme INT PRIMARY KEY,
            nota_imdb DECIMAL(3,1),
            FOREIGN KEY (id_filme) REFERENCES movies(id_filme)
                ON UPDATE CASCADE
                ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS filmes_rotten (
            id_filme INT PRIMARY KEY,
            nota_rotten DECIMAL(3,1),
            FOREIGN KEY (id_filme) REFERENCES movies(id_filme)
                ON UPDATE CASCADE
                ON DELETE CASCADE
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS vencedor_oscar (
            id_filme INT PRIMARY KEY,
            filme_oscar VARCHAR(100) NOT NULL UNIQUE,
            ano_oscar INT,
            categoria_oscar VARCHAR(50),
            FOREIGN KEY (id_filme) REFERENCES movies(id_filme)
                ON UPDATE CASCADE
                ON DELETE RESTRICT
        )
        """
    ]
    for comando in comandos:
        cursor.execute(comando)


conteudos = ler_csv()
print(conteudos)









