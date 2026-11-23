from model.Usuario import Usuario

class Bibliotecario(Usuario):
    def __init__(self, codigo: int, nome: str, login: str, senha: str):
        super().__init__(codigo, nome, login, senha)

    def getEmprestimosVisiveis(self, biblioteca) -> list:
        return list(biblioteca.getEmprestimos())

    def menu(self, biblioteca, dataAtual):
        opcao = None
        while opcao != "0":
            print(f"\n=== Menu Bibliotecário ({self.getNome()}) ===")
            print("1 - Visualizar todos os empréstimos")
            print("0 - Sair")
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                emprestimos = self.getEmprestimosVisiveis(biblioteca)
                if not emprestimos:
                    print("Nenhum empréstimo encontrado.")
                else:
                    for emp in emprestimos:
                        print(emp)
            elif opcao == "0":
                print(f"Até a próxima, {self.getNome()}.")
            else:
                print("Opção inválida.")