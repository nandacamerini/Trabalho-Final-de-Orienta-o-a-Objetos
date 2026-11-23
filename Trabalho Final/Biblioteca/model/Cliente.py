from pathlib import Path
from model.Usuario import Usuario

class Cliente(Usuario):
    def __init__(self, codigo: int, nome: str, login: str, senha: str):
        super().__init__(codigo, nome, login, senha)
        self.__emprestimos = []

    def getEmprestimos(self):
        pass
        #Emprestimo.getEmprestimosUsuario(self)

    def mostrarEmprestimosVisiveis(self):
        # mostra somente os empréstimos do cliente logado, com os 
        # livros, a data do empréstimo, a data de devolução prevista e a multa, se houver.
        for i in range(len(self.__emprestimos) - 1):
            print(self.__emprestimos[i])

    def visualizarLivros(self):
        # Mostrar todos os livros do acervo
        arquivo = Path(__file__).resolve().parent.parent / "livros.txt"
        try:
            with arquivo.open("r", encoding="utf-8") as livros:
                linhas = livros.readlines()
                
                for linha in linhas[1:]:
                    dadosLivros = linha.strip().split(";")

                    codigo = dadosLivros[0]
                    nome = dadosLivros[1]
                    autor = dadosLivros[2]

                    print(f"{codigo} - {nome} - {autor}")
                print()
        except FileNotFoundError:
            print(f"Arquivo livros.txt não encontrado.\n")

    def renovarEmprestimo(self):
        #  o cliente informa o código do empréstimo e o sistema renova, se as regras permitirem
        pass

    def visualizarSobre(self):
        # Falta decidir os dados do grupo (nome e função de cada integrante) e da empresafictícia (nome e história).
        pass

    def menu(self):
        escolhaUsuario = 0
        
        while escolhaUsuario != 5:
            print(f"1 - Visualizar Empréstimos \n"
                    "2 - Visualizar Livros \n"
                    "3 - Renovar Empréstimo \n"
                    "4 - Sobre \n"
                    "5 - Sair\n")

            escolhaUsuario = int(input("Escolha uma opção: "))
            # print vazio pra quebrar a linha
            print()

            if escolhaUsuario == 1:
                self.getEmprestimosVisiveis()
            
            elif escolhaUsuario == 2:
                self.visualizarLivros()
            
            elif escolhaUsuario == 3:
                self.renovarEmprestimo()

            elif escolhaUsuario == 4:
                self.visualizarSobre()

            elif escolhaUsuario == 5:
                print(f"Até a próxima {self.getNome()}")

            else:
                print("Número inválido")

    def __str__(self):
        return super().__str__()