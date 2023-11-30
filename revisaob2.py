import sqlite3

def criar_banco_dados():
    # Conectar ao banco de dados (criará o arquivo se não existir)
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    # Criar tabela livros
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            autor TEXT,
            ano_publicacao INTEGER
        )
    ''')

    # Salvar (commit) as alterações
    conn.commit()

    # Fechar conexão
    conn.close()

def inserir_livro(titulo, autor, ano_publicacao):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    # Inserir livro na tabela
    cursor.execute('''
        INSERT INTO livros (titulo, autor, ano_publicacao)
        VALUES (?, ?, ?)
    ''', (titulo, autor, ano_publicacao))

    # Salvar (commit) as alterações
    conn.commit()

    # Fechar conexão
    conn.close()

def consultar_livros():
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    # Selecionar e exibir todos os livros
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()

    for livro in livros:
        print(livro)

    # Fechar conexão
    conn.close()

def remover_livro(id_livro):
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()

    # Remover livro da tabela
    cursor.execute('DELETE FROM livros WHERE id = ?', (id_livro,))

    # Salvar (commit) as alterações
    conn.commit()

    # Fechar conexão
    conn.close()

def menu():
    while True:
        print("\n======= Menu =======")
        print("1. Inserir livro")
        print("2. Consultar livros")
        print("3. Remover livro")
        print("4. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano_publicacao = input("Digite o ano de publicação do livro: ")

            inserir_livro(titulo, autor, ano_publicacao)

        elif escolha == '2':
            consultar_livros()

        elif escolha == '3':
            id_livro = input("Digite o ID do livro a ser removido: ")
            remover_livro(id_livro)

        elif escolha == '4':
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    # Criar o banco de dados e a tabela se não existirem
    criar_banco_dados()

    # Iniciar o menu
    menu()