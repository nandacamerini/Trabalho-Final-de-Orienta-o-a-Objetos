from datetime import datetime, timedelta
from model.Cliente import Cliente
from model.Livro import Livro
class Emprestimo:

    PRAZO_DIAS = 14
    DIAS_RENOVACAO = 14
    MAX_RENOVACOES = 2
    MULTA_POR_DIA = 1.50
    MAX_LIVROS = 3

    def __init__(self, codigo: int, cliente: Cliente,
                data: datetime, renovacoes: int):

        if renovacoes < 0 or renovacoes > self.MAX_RENOVACOES:
            raise ValueError("Quantidade de renovações inválida.")

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
        return self.__livros.copy()

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
        if len(self.__livros) <= 1:
            return False

        if livro not in self.__livros:
            return False

        self.__livros.remove(livro)
        return True

    # Devoluções e multa
    def dataDevolucao(self):
        prazo = self.PRAZO_DIAS + (
            self.DIAS_RENOVACAO * self.__renovacoes
        )

        return self.__data + timedelta(days=prazo)

    def diasAtraso(self, dataAtual):
        dataPrevista = self.dataDevolucao()

        atraso = dataAtual.date() - dataPrevista.date()

        return max(0, atraso.days)

    def calcularMulta(self, dataAtual):
        dias = self.diasAtraso(dataAtual)
        quantidadeLivros = len(self.__livros)

        multa = dias * self.MULTA_POR_DIA * quantidadeLivros

        return multa

    # Renovações
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

    def __str__(self):
        codigosLivros = []

        for livro in self.__livros:
            codigosLivros.append(str(livro.getCodigo()))

        livros = ", ".join(codigosLivros)

        return (
            f"Código do empréstimo: {self.__codigo}\n"
            f"Código do cliente: {self.__cliente.getCodigo()}\n"
            f"Códigos dos livros: {livros}\n"
            f"Data do empréstimo: {self.__data.strftime('%d/%m/%Y')}\n"
            f"Data de devolução: "
            f"{self.dataDevolucao().strftime('%d/%m/%Y')}\n"
            f"Renovações: {self.__renovacoes}"
        )