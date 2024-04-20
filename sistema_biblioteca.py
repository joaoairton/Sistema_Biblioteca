class Livro:
    def __init__(self, titulo: str, autor: str, isbn: str, genero: str):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.genero = genero
        self.disponivel = True
        self.leitor_emprestimo = None

class Biblioteca:
    def __init__(self):
        self.lista_livros = []

    # Adicionar livro
    def adicionar_livro(self, livro: Livro) -> None:
        self.lista_livros.append(livro)
        print( f"O livro '{livro.titulo}' foi adicionado à biblioteca!" )

    # Remover livro
    def remover_livro(self, livro: Livro) -> None:
        if livro in self.lista_livros:
            self.lista_livros.remove(livro)
            print( f"O livro '{livro.titulo}' foi removido da biblioteca!" )
        else:
            print( f"O livro '{livro.titulo}' não está na biblioteca!" )

    # Editar livro
    def editar_livro(self, livro: Livro, novo_titulo=None, novo_autor=None, novo_isbn=None, novo_genero=None) -> None:
        if livro in self.lista_livros:
            livro.titulo = novo_titulo or livro.titulo
            livro.autor = novo_autor or livro.autor
            livro.isbn = novo_isbn or livro.isbn
            livro.genero = novo_genero or livro.genero
            print( f"O livro '{livro.titulo}' foi atualizado com sucesso." )
        else:
            print( f"O livro '{livro.titulo}' não está na biblioteca." )

    # Pesquisar livro
    def pesquisar_livro(self, titulo: str) -> Livro:
        for livro in self.lista_livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None

    # Exibir livros da Biblioteca
    def exibir_livros(self) -> None:
        if not self.lista_livros:
            print( "Não há livros disponíveis na biblioteca!" )
        else:
            print( "Livros disponíveis na biblioteca: " )
            for livro in self.lista_livros:
                print( f"Título: {livro.titulo}, Autor: {livro.autor}, ISBN: {livro.isbn}, Gênero: {livro.genero}" )
                print("-" * 30)

    # Emprestar livro
    def emprestar_livro(self, livro: Livro, leitor: str) -> None:
        if livro in self.lista_livros:
            if livro.disponivel:
                livro.disponivel = False
                livro.leitor_emprestimo = leitor
                print( f"O livro '{livro.titulo}' foi emprestado para {leitor}." )
            else:
                print( f"O livro '{livro.titulo}' já está emprestado." )
        else:
            print( f"O livro '{livro.titulo}' não está na biblioteca." )

    # Devolver livro
    def devolver_livro(self, livro: Livro) -> None:
        if livro in self.lista_livros:
            if not livro.disponivel:
                livro.disponivel = True
                livro.leitor_emprestimo = None
                print( f"O livro '{livro.titulo}' foi devolvido!" )
            else:
                print( f"O livro '{livro.titulo}' já está disponível na biblioteca." )
        else:
            print( f"O livro '{livro.titulo}' não está na biblioteca." )
            