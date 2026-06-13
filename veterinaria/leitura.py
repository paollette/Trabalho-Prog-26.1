import ast
from paciente import Paciente

def ler_arquivo(path):
    pacientes = []
    
    with open(path, "r", encoding='utf-8') as f:

        next(f, None) # a leitura de arquivos barra com o cabeçalho da fgeradora.py, então adicionei este trecho.
                      # sem ele, ast.literal_eval leria a str() cabeçalho tentando encontrar uma list(), ou seja, vai dar erro.

        for linha in f:
            partes = linha.strip().split(";")
            if not partes or partes == ['']: 
                continue
            
            identidade_, nome, especie, idade, peso, tratamentos_str, cadastro_str = partes[:7] # como há menos variáveis, partes[:9] foi para partes[:7]

            # de: id_, nome, especie, raça, coloraçao, idade, peso, diagnostico_str, cadastro_str
            # para: identidade_, nome, especie, idade, peso, tratamentos_str, cadastro_str

            # CONVERSÃO DE TIPOS - com variáveis alteradas.
            tratamentos = ast.literal_eval(tratamentos_str)
            cadastro = ast.literal_eval(cadastro_str)

            paciente = Paciente(identidade_, nome, especie, idade, peso, tratamentos, cadastro) 
            pacientes.append(paciente)
            
    return pacientes


# o codigo original ta aqui embaixo:

# import ast
# from paciente import Paciente

# def ler_arquivo(path):
#     pacientes = []
    
#     with open(path, "r", encoding='utf-8') as f:
#         for linha in f:
#             partes = linha.strip().split(";")
#             if not partes or partes == ['']: 
#                 continue
            
#             id_, nome, especie, raça, coloraçao, idade, peso, diagnostico_str, cadastro_str = partes[:9] 

#             # CONVERSÃO DE TIPOS
#             diagnostico = ast.literal_eval(diagnostico_str)
#             cadastro = ast.literal_eval(cadastro_str)

#             paciente = Paciente(id_, nome, especie, raça, coloraçao, idade, peso, diagnostico, cadastro)

#             pacientes.append(paciente)
            
#     return pacientes
