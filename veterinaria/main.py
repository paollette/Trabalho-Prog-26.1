import time
import crud

# ========== ESCOLHA DO ARQUIVO ==========
print("""
╔══════════════════════════════════╗
║         🐾 PAW CENTER 🐾         ║
╠══════════════════════════════════╣
║  Qual arquivo deseja alterar?    ║
╠══════════════════════════════════╣
║  0 - pequeno.txt                 ║
║  1 - medio.txt                   ║
║  2 - grande.txt                  ║
║  3 - gigante.txt                 ║
╚══════════════════════════════════╝
""")
arquivos = ["data\\pequeno.txt", "data\\medio.txt", "data\\grande.txt", "data\\gigante.txt"]
x = int(input("Qual arquivo deseja carregar? "))

# ========== LEITURA ==========
print("\nCarregando base de dados de pacientes...")
inicio = time.perf_counter()
crud.carregar(arquivos[x])
fim = time.perf_counter()
print(f"Base carregada com sucesso!")
print(f"Tempo de leitura: {fim - inicio:.4f} segundos.")

# ========== MENU ==========
flag = True
while flag:
    print("""
╔══════════════════════════════════╗
║         🐾 PAW CENTER 🐾         ║
╠══════════════════════════════════╣
║  0 - Buscar animal               ║
║  1 - Adicionar animal            ║
║  2 - Remover animal              ║
║  3 - Sair                        ║
╚══════════════════════════════════╝
""")

    try:
        r = int(input("O que deseja? "))

        if r == 0:
            id_busca = int(input("Digite um ID para buscar: "))
            inicio = time.perf_counter()
            crud.buscar_animais(crud.pacientes, id_busca)
            fim = time.perf_counter()
            print(f"Tempo de busca: {fim - inicio:.4f} segundos.")
            input("\nPressione Enter para continuar...")

        elif r == 1:
            inicio = time.perf_counter()
            crud.adicionar_animais(crud.pacientes)
            fim = time.perf_counter()
            crud.salvar(crud.arq, crud.pacientes)
            print(f"Tempo de adição: {fim - inicio:.4f} segundos.")
            input("\nPressione Enter para continuar...")

        elif r == 2:
            id_remocao = int(input("Digite um ID para remover: "))
            inicio = time.perf_counter()
            crud.remover_animais(crud.pacientes, id_remocao)
            fim = time.perf_counter()
            crud.salvar(crud.arq, crud.pacientes)
            print(f"Tempo de remoção: {fim - inicio:.4f} segundos.")
            input("\nPressione Enter para continuar...")

        elif r == 3:
            print("\nAté logo! 🐾")
            flag = False

        else:
            print("Opção inválida!")

    except ValueError:
        print("Entrada inválida, tente novamente.")
