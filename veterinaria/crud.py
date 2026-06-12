from leitura import ler_arquivo

# Lista global
pacientes = []
arq = None

def carregar(arquivo):
    global pacientes, arq
    arq = arquivo
    pacientes = ler_arquivo(arq)

# parte pra tu antonio