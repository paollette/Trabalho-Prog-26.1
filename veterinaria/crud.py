from leitura import ler_arquivo

# Lista global
pacientes = []
arq = None

def carregar(arquivo):
    global pacientes, arq
    arq = arquivo
    pacientes = ler_arquivo(arq)


def adicionar_animais(pacientes, animal):
    pacientes.append(animal)
    print("Animalzinho adicionado!")
    

def remover_animais(pacientes, id_removido):
    for i in range(len(pacientes)):
        if pacientes[i].identidade == id_removido: # pacientes[i]["identidade"] para pacientes[i].identidade, já que estamos lidando com o uso de endereços class.
            pacientes.pop(i)                       # uso de indíces pra dicionários não funcionaria.
            print("Animal removido!")
            return
    print("Animal não encontrado!")


def buscar_animais(pacientes, id_procurado): # Dar uma olhada se os nomes das variáveis e ordem estão corretos, acredito que tenha ajustado, mas vai que...
    for animal in pacientes:
        if animal.identidade == id_procurado: # animal["identidade"] para animal.identidade, pelo uso de class.
            print(f"""
                Id:           {animal.identidade}
                Nome:         {animal.nome}
                Espécie:      {animal.especie}
                Idade:        {animal.idade}
                Peso:         {animal.peso}
                Tratamentos:  {animal.tratamentos}
                Cadastro:     {animal.cadastro}
            """)
            return
    # o loop tem que acabar quando acha o id, adicionei o return.
    # corrigi o nome das variáveis com todo o restante de código. 
    print("Animal não encontrado!")


# DEBUG

flag = True

# arquivos
arq = ["data\\pequeno.txt", "data\\medio.txt", "data\\grande.txt", "data\\gigante.txt"]
x = int(input("0 - pequeno.txt\n1 - medio.txt\n2 - grande.txt\n3 - gigante.txt\nler qual arquivo? "))
carregar(arq[x])

# interface - só fiz pra testar tudo.

print("\nVETERINARIA KOWADA CEIFEIRO COLOMBO DA MORTE\n")

while flag:

    r = int(input("0 - buscar\n1 - adicionar\n2 - remover\n3 - sair\nO QUE DESEJA? "))

    if r in [0, 1, 2, 3]:

        try:
            if r == 0:
                id_busca = int(input("Digite um ID para buscar (ex: 1): "))
                buscar_animais(pacientes, id_busca) # busca funcional
                input("pressione Enter para continuar...")

            elif r == 1:
                id_add = int(input("Digite um ID para adicionar (ex: 1): "))
                adicionar_animais(pacientes, id_add) # não adiciona ninguém efetivamente.
                input("pressione Enter para continuar...")
            
            elif r == 2:
                id_remocao = int(input("Digite um ID para remover (ex: 1): "))
                remover_animais(pacientes, id_remocao) # remove sim mas não no arquivo original, eu acho.
                input("pressione Enter para continuar...")

            elif r == 3:
                flag = False
                continue

        except:
            r = int(input("0 - buscar\n1 - adicionar\n2 - remover\nO QUE DESEJA? "))
