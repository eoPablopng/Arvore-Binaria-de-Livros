class Livro:
    def __init__(self, ISBN, Titulo, Valor, Autor, Editora, Ano):
        self.ISBN = ISBN
        self.Titulo = Titulo
        self.Valor = Valor
        self.Autor = Autor
        self.Editora = Editora
        self.Ano = Ano
        self.esquerda = None
        self.direita = None


def criar():
    return None


def acrescentar(raiz, livro):
    if raiz is None:
        return livro
    if livro.ISBN < raiz.ISBN:
        raiz.esquerda = acrescentar(raiz.esquerda, livro)
    elif livro.ISBN > raiz.ISBN:
        raiz.direita = acrescentar(raiz.direita, livro)
    else:
        print("⚠️ Livro com ISBN já existe na árvore.")
    return raiz


def exibir(raiz):
    if raiz:
        exibir(raiz.esquerda)
        print(f"{raiz.ISBN} - {raiz.Titulo} ({raiz.Ano}) - R${raiz.Valor:.2f}")
        exibir(raiz.direita)


if __name__ == "__main__":
    arvore = criar()

    # Criando livros
    livro1 = Livro(9788595083278, "A Habilidade de Ligar o FDS", 45.90, "Desconhecido", "Editora Alpha", 2023)
    livro2 = Livro(9786559820801, "Jujutsu Kaisen 0", 34.90, "Gege Akutami", "Panini", 2021)
    livro3 = Livro(9786559600663, "Demon Slayer", 29.90, "Koyoharu Gotouge", "Panini", 2020)

    # Inserindo na árvore
    arvore = acrescentar(arvore, livro1)
    arvore = acrescentar(arvore, livro2)
    arvore = acrescentar(arvore, livro3)

    print("📚 Livros na árvore binária de busca (ordenados por ISBN):")
    exibir(arvore)
