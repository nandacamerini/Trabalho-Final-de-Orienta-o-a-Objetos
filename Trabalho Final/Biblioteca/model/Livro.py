class Livro:
    def __init__(self, codigo: int, nome: str, autor: str):
        self.__codigo = codigo
        self.__nome = nome
        self.__autor = autor

    def __str__(self):
        return f"Código: {self.__codigo} | Nome: {self.__nome} | Autor: {self.__autor}"