from model.Cliente import Cliente
from model.Biblioteca import Biblioteca
def principal():
    # Teste das funções do Cliente.py (a parte de login tem que ficar no Biblioteca.py)
    biblioteca = Biblioteca()
    biblioteca.carregarArquivos()

if __name__ == "__main__":
    principal()