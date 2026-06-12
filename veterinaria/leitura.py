import ast
from paciente import Paciente

def ler_arquivo(path):
    pacientes = []
    
    with open(path, "r", encoding='utf-8') as f:
        for linha in f:
            partes = linha.strip().split(";")
            if not partes or partes == ['']: 
                continue
            
            id_, nome, especie, raça, coloraçao, idade, peso, diagnostico_str, cadastro_str = partes[:9]

            # CONVERSÃO DE TIPOS
            diagnostico = ast.literal_eval(diagnostico_str)
            cadastro = ast.literal_eval(cadastro_str)

            paciente = Paciente(id_, nome, especie, raça, coloraçao, idade, peso, diagnostico, cadastro)

            pacientes.append(paciente)
            
    return pacientes