from model.Cliente import Cliente
from model.Biblioteca import Biblioteca
from datetime import datetime
def principal():
    # Teste das funções do Cliente.py (a parte de login tem que ficar no Biblioteca.py)
    biblioteca = Biblioteca()
    biblioteca.carregarArquivos()

    dataAtual = datetime(2026, 11, 23)

    print("\n===== TESTE DE RENOVAÇÕES =====")

    for emprestimo in biblioteca.getEmprestimos():
        resultado = emprestimo.renovar(dataAtual)

        print(f"\nEmpréstimo: {emprestimo.getCodigo()}")

        if resultado:
            print("Renovação realizada!")
        else:
            print("Não foi possível renovar.")

        print(f"Quantidade de renovações: {emprestimo.getRenovacoes()}")
        print(f"Nova data de devolução: {emprestimo.dataDevolucao().strftime('%d/%m/%Y')}")

if __name__ == "__main__":
    principal()