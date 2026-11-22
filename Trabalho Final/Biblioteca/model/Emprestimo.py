from pathlib import Path

class Emprestimo:
    def __init__(self, codigo: int, codigoCliente: int, codigoLivro: int, data, renovacoes: int):
        self.__codigo = codigo
        self.__codigoCliente = codigoCliente
        self.__codigoLivro = codigoLivro
        self.__data = data
        self.__renovacoes = renovacoes

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
        return f"Código: {self.__codigo} | Código do cliente: {self.__codigoCliente} | Código do livro: {self.__codigoLivro} | Data: {self.__data} | Renovações: {self.__renovacoes}"