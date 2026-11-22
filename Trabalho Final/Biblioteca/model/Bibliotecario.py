from model.Usuario import Usuario

class Bibliotecario(Usuario):
    def __init__(self, codigo: int, nome: str, login: str, senha: str):
        super().__init__(codigo, nome, login, senha)

    def menu(self):
        pass