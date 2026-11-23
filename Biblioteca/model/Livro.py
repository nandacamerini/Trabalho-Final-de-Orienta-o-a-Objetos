class Livro:

    def __init__(self, codigo: int, nome: str, autor: str):
        self.__codigo = codigo
        self.__nome = nome
        self.__autor = autor

    def getCodigo(self) -> int:
        return self.__codigo

    def getNome(self) -> str:
        return self.__nome

    def getAutor(self) -> str:
        return self.__autor

    def setNome(self, nome: str):
        self.__nome = nome

    def setAutor(self, autor: str):
        self.__autor = autor

    def __str__(self) -> str:
        return f"Código: {self.__codigo} | Nome: {self.__nome} | Autor: {self.__autor}"