from datetime import datetime, timedelta
from pathlib import Path
from model.Cliente import Cliente
from model.Livro import Livro
class Emprestimo:

    PRAZO_DIAS = 14
    DIAS_RENOVACAO = 14
    MAX_RENOVACOES = 2
    MULTA_POR_DIA = 1.50
    MAX_LIVROS = 3

    def __init__(self, codigo: int, cliente: Cliente, data: datetime, renovacoes: int):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__livros = []
        self.__data = data
        self.__renovacoes = renovacoes

    def addLivro(self, livro):
        if len(self.__livros) >= self.MAX_LIVROS:
            return False

        if livro in self.__livros:
            return False

        self.__livros.append(livro)
        return True

    def getLivros(self):
            return self.__livros
    
    def getEmprestimosUsuario(self, usuario):
        listaEmprestimos = []
        arquivo = Path(__file__).resolve().parent.parent / "emprestimos.txt"
        try:
            with arquivo.open("r", encoding="utf-8") as emprestimos:
                linhas = emprestimos.readlines()

                print(f"Empréstimos de {usuario.getNome()}")
                for linha in linhas[1:]:
                    dados = linha.strip().split(";")

                    if dados[1] == usuario.getCodigo():
                        listaEmprestimos.append(f"Código do livro: {dados[2]}," 
                                                "data inicial: {dados[3]},"
                                                "data de devolução: ")
        except FileNotFoundError:
            print(f"Arquivo emprestimos.txt não encontrado.\n")

    def __str__(self):
        return f"Código: {self.__codigo} | Código do cliente: {self.__cliente} | Código do livro: {self.__livros} | Data: {self.__data} | Renovações: {self.__renovacoes}"