from leitura import ler_arquivo

# Lista global
pacientes = []
arq = None

def carregar(arquivo):
    global pacientes, arq
    arq = arquivo
    pacientes = ler_arquivo(arq)


def adicionar_animais(pacientes):
    identidade  = input("ID: ")
    nome        = input("Nome: ")
    especie     = input("Espécie: ")
    idade       = input("Idade: ")
    peso        = input("Peso: ")
    tratamentos = input("Tratamentos (ex: banho, vacina): ").split(", ")
    cadastro    = input("Cadastrado? (True/False): ")

    novo_animal = Paciente(identidade, nome, especie, idade, peso, tratamentos, cadastro)
    pacientes.append(novo_animal)
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


def salvar_animais(nome_arquivo, pacientes):
   with open(nome_arquivo, "w", encoding='utf-8') as f:
        f.write("IDENTIDADE NOME ESPECIE IDADE PESO TRATAMENTOS CADASTRO\n") #AYRAM, DEPOIS MUDA AQUI DO JEITO QUE ESTAVA O CABEÇALHO
        for animal in pacientes:
            f.write(animal.para_linha()) #usei a função para_linha() que você fez, depois verifica se é isso mesmo

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
                adicionar_animais(pacientes)
                salvar(arq[x], pacientes)
                input("pressione Enter para continuar...")

            
            elif r == 2:
                id_remocao = int(input("Digite um ID para remover (ex: 1): "))
                remover_animais(pacientes, id_remocao) 
                salvar(arq[x], pacientes) #chamei a função para salvar no arquivo
                input("pressione Enter para continuar...")

            elif r == 3:
                flag = False
                continue

        except:
            r = int(input("0 - buscar\n1 - adicionar\n2 - remover\nO QUE DESEJA? "))
