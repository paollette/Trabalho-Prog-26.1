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
        if pacientes[i]["identidade"] == id_removido:
            pacientes.pop(i)
            print("Animal removido!")
            return
    print("Animal não encontrado!")


def buscar_animais(pacientes, id_procurado): #Dar uma olhada se os nomes das variáveis e ordem estão corretos, acredito que tenha ajustado, mas vai que...
    for animal in pacientes:
        if animal["identidade"] == id_procurado:
            print(f"""
                Id:           {animal['identidade']}
                Nome:         {animal['nome']}
                Espécie:      {animal['especie']}
                Idade:        {animal['idade']}
                Peso:         {animal['peso']}
                Cadastro:     {animal['cadastro']}
                Procedimento: {animal['procedimentos_formatado']}
                
            """)
    print("Animal não encontrado!")
