import time
import random


NOMES = ['Luna', 'Thor','Mel', 'Paçoca', 'Pipoca', 'Bento', 'Amora', 'Simba', 'Zeca', 'Nina', 'Theo', 'Lola', 'Koda', 'Gaia', 'Otto',
          'Jade', 'Café', 'Cookie', 'Sushi', 'Alecrim', 'Pudim', 'Tequila', 'Cacau', 'Jujuba', 'Yoda', 'Arya', 'Loki', 'Zelda', 'Stitch',
            'Sherlock', 'Frodo', 'Nala', 'Arthur', 'Alice', 'Bento', 'Cecília', 'Joaquim', 'Clara', 'Vicente', 'Flora']

ESPECIES = ['Cachorro', 'Gato', 'Coelho', 'Hamster', 'Porquinho-da-india', 'Calopsita', 'Peixe-dourado', 'Tartaruga']

PROCEDIMENTOS = ['Consulta_rotina', 'Vacinação', 'Castração', 'Limpeza_tártaro', 'Hemograma', 'Ultrassonografia', 'Curativo_ferida']


def gerar_pets(identidade):

    nome = random.choice(NOMES)
    especie = random.choice(ESPECIES)
    idade = random.randint(1, 15)
    peso = round(random.uniform(0.5, 40.0), 2) # round(número a ser arredondado, casas decimais) - uniform(ínicio, fim) gera um float dentro de um intervalo.
    cadastro = random.choice([True, False])

    procedimentos_qtd = random.randint(1, 3)
    procedimentos_lista = random.sample(PROCEDIMENTOS, procedimentos_qtd) # sample() é o mesmo que choice, mas ao invés de um elemento único, n elementos únicos dentro da lista.
    procedimentos_formatado = ";".join(procedimentos_lista) # listas naturalmente são separadas por "," que gera problema no CSV que identifica como coluna.

    return f"{identidade},{nome},{especie},{idade},{peso},{cadastro},{procedimentos_formatado}\n"


def gerar_arquivo_dados(nome_arquivo, qtd_linhas):
    
    tempo_inicio = time.perf_counter() # contador marca horário de começo.

    with open(nome_arquivo, "w", encoding="utf-8") as file:

        file.write("ID,NOME,ESPECIE,IDADE,PESO,CADASTRO_ATIVO,PROCEDIMENTOS\n") # cabeçalho inicial

        for i in range(1, qtd_linhas + 1): # aqui imprimimos pacientes aleátórios conforme a quantidade de linhas que definimos pros tamanhos dos arquivos.
            dados_por_linha = gerar_pets(i) # o ID responsável pela criação do pet.
            file.write(dados_por_linha) # aqui retorna a função anteirior escrita no arquivo.
            
    tempo_fim = time.perf_counter() # contador marca horário final.
    tempo_total = tempo_fim - tempo_inicio # traz o tempo necessário para rodar o programa.
    
    print(f"Arquivo '{nome_arquivo}' finalizado.")
    print(f"Tempo de processamento: {tempo_total:.4f} segundos.\n")
    
    return tempo_total

       
print("DEBUG")                            # resultados do meu PC: ("\" pra Windows, "/" pra Linux)
gerar_arquivo_dados("data\pequeno.csv", 100)      # 100 pacientes (0.0008 segundos)
gerar_arquivo_dados("data\medio.csv", 10000)      # 10 mil pacientes (0.0488 segundos)
gerar_arquivo_dados("data\grande.csv", 100000)    # 100 mil pacientes (0.4699 segundos)
gerar_arquivo_dados("data\gigante.csv", 1000000)  # 1 milhão de pacientes (4.9325 segundos)
