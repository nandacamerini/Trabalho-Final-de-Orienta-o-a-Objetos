from model.Biblioteca import Biblioteca
from datetime import datetime


def principal():
    dataAtual = datetime.now()

    # Carrega os arquivos
    biblioteca = Biblioteca()
    biblioteca.carregarArquivos()

    # Busca o cliente
    cliente = biblioteca.buscarCliente(3)

    if cliente is None:
        print("Cliente não encontrado.")
        return

    print("=" * 45)
    print("       TESTE DO SISTEMA DE BIBLIOTECA")
    print("=" * 45)

    # TESTE 1: Visualizar empréstimos e multas
    print("\n===== TESTE 1: EMPRÉSTIMOS E MULTAS =====")
    cliente.mostrarEmprestimosVisiveis(biblioteca, dataAtual)

    # TESTE 2: Renovar um empréstimo
    print("\n===== TESTE 2: RENOVAÇÃO DE EMPRÉSTIMO =====")
    cliente.renovarEmprestimo(biblioteca, dataAtual)

    # TESTE 3: Verificar se a renovação foi salva
    print("\n===== TESTE 3: VERIFICAR GRAVAÇÃO NO TXT =====")

    novaBiblioteca = Biblioteca()
    novaBiblioteca.carregarArquivos()

    novoCliente = novaBiblioteca.buscarCliente(3)

    if novoCliente is None:
        print("Não foi possível carregar o cliente novamente.")
        return

    novoCliente.mostrarEmprestimosVisiveis(novaBiblioteca, dataAtual)

    print("\n===== FIM DOS TESTES =====")


if __name__ == "__main__":
    principal()