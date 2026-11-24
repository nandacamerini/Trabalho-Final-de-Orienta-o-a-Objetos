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

    def getCodigo(self):
        return self.__codigo

    def getCliente(self):
        return self.__cliente

    def getDataEmprestimo(self):
        return self.__data

    def getLivros(self):
        return self.__livros

    def getRenovacoes(self):
        return self.__renovacoes

    def addLivro(self, livro: Livro):
        if len(self.__livros) >= self.MAX_LIVROS:
            return False

        if livro in self.__livros:
            return False

        self.__livros.append(livro)
        return True

    def removeLivro(self, livro: Livro):
        if len(self.__livros) <= 0:
            return False

        if livro not in self.__livros:
            return False

        self.__livros.remove(livro)
        return True

    #Devoluções e multa
    def dataDevolucao(self):
        prazo = self.PRAZO_DIAS + (self.DIAS_RENOVACAO * self.__renovacoes)

        return self.__data + timedelta(days=prazo)

    def diasAtraso(self, dataAtual):
        dataPrevista = self.dataDevolucao()

        if dataAtual <= dataPrevista:
            return 0

        atraso = dataAtual - dataPrevista

        return atraso.days

    def calcularMulta(self, dataAtual):
        dias = self.diasAtraso(dataAtual)
        quantidadeLivros = len(self.__livros)

        multa = dias * self.MULTA_POR_DIA * quantidadeLivros

        return multa

    #Renovações
    def podeRenovar(self, dataAtual):
        if self.__renovacoes >= self.MAX_RENOVACOES:
            return False

        if self.diasAtraso(dataAtual) > 0:
            return False

        return True

    def renovar(self, dataAtual):
        if not self.podeRenovar(dataAtual):
            return False

        self.__renovacoes += 1

        return True



    
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
        codigosLivros = []

        for livro in self.__livros:
            codigosLivros.append(str(livro.getCodigo()))

        livros = ", ".join(codigosLivros)

        return (f"Código do empréstimo: {self.__codigo}\n"
                f"Código do cliente: {self.__cliente.getCodigo()}\n"
                f"Códigos dos livros: {livros}\n"
                f"Data do empréstimo: {self.__data.strftime('%d/%m/%Y')}\n"
                f"Data de devolução: {self.dataDevolucao().strftime('%d/%m/%Y')}\n"
                f"Renovações: {self.__renovacoes}")