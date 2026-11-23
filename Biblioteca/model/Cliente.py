from pathlib import Path
from model.Usuario import Usuario

class Cliente(Usuario):
    def __init__(self, codigo: int, nome: str, login: str, senha: str):
        super().__init__(codigo, nome, login, senha)

    def getEmprestimosVisiveis(self, biblioteca) -> list:
        visiveis = []
        for emprestimo in biblioteca.getEmprestimos():
            cliente_emp = emprestimo.getCliente()
            if cliente_emp is not None and cliente_emp.getCodigo() == self.getCodigo():
                visiveis.append(emprestimo)
        return visiveis

    def mostrarEmprestimosVisiveis(self, biblioteca, dataAtual=None):
        emprestimos = self.getEmprestimosVisiveis(biblioteca)
        if not emprestimos:
            print("Você não possui empréstimos.\n")
            return

        for emp in emprestimos:
            print(emp)
        print()

    def visualizarLivros(self):
        # Mostrar todos os livros do acervo
        arquivo = Path(__file__).resolve().parent.parent / "livros.txt"
        try:
            with arquivo.open("r", encoding="utf-8") as livros:
                linhas = livros.readlines()

                for linha in linhas[1:]:
                    linha = linha.strip()
                    if not linha:
                        continue

                    dadosLivros = linha.split(";")
                    if len(dadosLivros) >= 3:
                        codigo = dadosLivros[0]
                        nome = dadosLivros[1]
                        autor = dadosLivros[2]
                        print(f"{codigo} - {nome} - {autor}")
                print()
        except FileNotFoundError:
            print("Arquivo livros.txt não encontrado.\n")

    def renovarEmprestimo(self, biblioteca, dataAtual):
        # O cliente informa o código do empréstimo e o sistema renova, se as regras permitirem
        pass

    def visualizarSobre(self):
        # Falta decidir os dados
        pass

    def menu(self, biblioteca, dataAtual):
        escolhaUsuario = 0

        while escolhaUsuario != 5:
            print(
                "1 - Visualizar Empréstimos\n"
                "2 - Visualizar Livros\n"
                "3 - Renovar Empréstimo\n"
                "4 - Sobre\n"
                "5 - Sair\n"
            )

            try:
                escolhaUsuario = int(input("Escolha uma opção: "))
            except ValueError:
                print("Número inválido\n")
                continue

            print()

            if escolhaUsuario == 1:
                self.mostrarEmprestimosVisiveis(biblioteca, dataAtual)

            elif escolhaUsuario == 2:
                self.visualizarLivros()

            elif escolhaUsuario == 3:
                self.renovarEmprestimo(biblioteca, dataAtual)

            elif escolhaUsuario == 4:
                self.visualizarSobre()

            elif escolhaUsuario == 5:
                print(f"Até a próxima {self.getNome()}")

            else:
                print("Número inválido\n")

    def __str__(self):
        return super().__str__()