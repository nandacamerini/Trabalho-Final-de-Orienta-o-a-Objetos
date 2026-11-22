from pathlib import Path
from model.Usuario import Usuario
from model.Cliente import Cliente
from model.Bibliotecario import Bibliotecario
from model.Livro import Livro
from model.Emprestimo import Emprestimo

class Biblioteca():
    def __init__(self):
        self.__usuarios = []
        self.__livros = []
        self.__emprestimos = []

    def getUsuarios(self):
        return self.__usuarios

    def addUsuario(self, usuario: Usuario):
        self.__usuarios.append(usuario)

    def removeUsuario(self, usuario: Usuario):
        if usuario in self.__usuarios:
            self.__usuarios.remove(usuario)

    def addLivros(self, livro: Livro):
        self.__livros.append(livro)

    def removeLivro(self, livro: Livro):
        if livro in self.__livros:
            self.__livros.remove(livro)

    def addEmprestimo(self, empresimo: Emprestimo):
        self.__emprestimos.append(empresimo)

    def removeEmprestimo(self, emprestimo: Emprestimo):
        if emprestimo in self.__emprestimos:
            self.__emprestimos.remove(emprestimo)

    def lerArquivo(self, caminhoArquivo):
        dados = []

        try:
            with open(caminhoArquivo, "r", encoding="utf-8") as arquivo:
                next(arquivo, None)

                for numero_linha, linha in enumerate(arquivo, start=2):
                    linha = linha.strip()

                    if not linha:
                        continue

                    partes = linha.split(";")

                    dados.append(partes)

            return dados

        except FileNotFoundError:
            print(f"Arquivo {caminhoArquivo} não encontrado.")
            return []

    def carregarUsuarios(self, caminhoArquivo):
        dados = self.lerArquivo(caminhoArquivo)
        for partes in dados:

            if len(partes) != 5:
                continue

            codigo = int(partes[0])
            nome = partes[1]
            tipo_usuario = partes[2]
            login = partes[3]
            senha_hash = partes[4]

            if tipo_usuario == "Cliente":
                usuario = Cliente(codigo, nome, login, senha_hash)
                self.addUsuario(usuario)

            elif tipo_usuario == "Bibliotecario":
                usuario = Bibliotecario(codigo, nome, login, senha_hash)
                self.addUsuario(usuario)
        #debug
        print("usuário instanciados")
        for i in range(len(self.__usuarios)):
            print(self.__usuarios[i])

    def carregarLivros(self, caminhoArquivo):
        dados = self.lerArquivo(caminhoArquivo)
        for partes in dados:

            if len(partes) != 3:
                continue

            codigo = int(partes[0])
            nome = partes[1]
            autor = partes[2]

            livro = Livro(codigo, nome, autor)
            self.addLivros(livro)
        #debug
        print("livros instanciados")
        for i in range(len(self.__livros)):
            print(self.__livros[i])

    def carregarEmprestimos(self, caminhoArquivo):
        dados = self.lerArquivo(caminhoArquivo)
        for partes in dados:

            if len(partes) != 5:
                continue

            codigo = int(partes[0])
            codigoCliente = int(partes[1])
            codigoLivro = int(partes[2])
            data = partes[3]
            renovacoes = int(partes[4])

            emprestimo = Emprestimo(codigo, codigoCliente, codigoLivro, data, renovacoes)
            self.addEmprestimo(emprestimo)
        #debug
        print("Empréstimos instanciados")
        for i in range(len(self.__emprestimos)):
            print(self.__emprestimos[i])

    def carregarArquivos(self):
        #Carrega e instancia os objetos dos usuários, livros e emprestimos
        caminhoUsuarios = Path(__file__).resolve().parent.parent / "usuarios.txt"
        caminhoLivros = Path(__file__).resolve().parent.parent / "livros.txt"
        caminhoEmprestimos = Path(__file__).resolve().parent.parent / "emprestimos.txt"

        self.carregarUsuarios(caminhoUsuarios)
        self.carregarLivros(caminhoLivros)
        self.carregarEmprestimos(caminhoEmprestimos)