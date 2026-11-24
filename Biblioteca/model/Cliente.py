from pathlib import Path
from model.Usuario import Usuario

class Cliente(Usuario):
    def __init__(self, codigo: int, nome: str, login: str, senha: str):
        super().__init__(codigo, nome, login, senha)

    def getEmprestimosVisiveis(self, biblioteca) -> list:
        return biblioteca.getEmprestimosUsuario(self)

    def mostrarEmprestimosVisiveis(self, biblioteca, dataAtual):
        emprestimos = self.getEmprestimosVisiveis(biblioteca)

        if not emprestimos:
            print("Você não possui empréstimos.\n")
            return

        for emp in emprestimos:
            print(emp)

            multa = emp.calcularMulta(dataAtual)

            if multa > 0:
                valorMulta = f"{multa:.2f}".replace(".", ",")
                print(f"Multa por atraso: R$ {valorMulta}")

            print("-" * 40)

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
        # Busca os empréstimos do cliente
        emprestimos = self.getEmprestimosVisiveis(biblioteca)

        if not emprestimos:
            print("Você não possui empréstimos para renovar.\n")
            return

        # Mostra os empréstimos disponíveis
        self.mostrarEmprestimosVisiveis(biblioteca, dataAtual)

        # Solicita o código do empréstimo
        try:
            codigo = int(input(
                "Digite o código do empréstimo que deseja renovar: "
            ))
        except ValueError:
            print("Código inválido.\n")
            return

        # Procura o empréstimo escolhido
        emprestimoEscolhido = None

        for emprestimo in emprestimos:
            if emprestimo.getCodigo() == codigo:
                emprestimoEscolhido = emprestimo
                break

        # Verifica se o empréstimo foi encontrado
        if emprestimoEscolhido is None:
            print("Empréstimo não encontrado.\n")
            return

        # Tenta realizar a renovação
        if emprestimoEscolhido.renovar(dataAtual):
            if biblioteca.salvarEmprestimos():
                print("Empréstimo renovado e salvo com sucesso!")

                print(
                    f"Nova data de devolução: "
                    f"{emprestimoEscolhido.dataDevolucao().strftime('%d/%m/%Y')}\n"
                )
            else:
                print("A renovação foi realizada, mas não foi possível salvá-la no arquivo.")
                print("Tente salvar novamente antes de fechar o programa.\n")
        else:
            print("Não foi possível renovar o empréstimo.")
            print(
                "Verifique se ele está atrasado ou se já atingiu "
                "o limite de renovações.\n"
            )

    def visualizarSobre(self):
        # Falta decidir os dados com o grupo
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