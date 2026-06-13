class Paciente:
    def __init__(self, identidade_, nome, especie, idade, peso, tratamentos, cadastro):
        self.identidade = int(identidade_)
        self.nome = nome
        self.especie = especie
        self.idade = int(idade)
        self.peso = float(peso)
        self.tratamentos = tratamentos
        self.cadastro = bool(cadastro)
        # retirei variáveis sobressalentes (raça, coloracao), alterei nomes (id e diagnostico para identidade e tratamentos)

    def para_linha(self):
        return f"{self.identidade};{self.nome};{self.especie};{self.idade};{self.peso};{self.tratamentos};{self.cadastro}\n"
    # retirei variáveis sobressalentes (raça, coloracao), alterei nomes (id e diagnostico para identidade e tratamentos)

    def __repr__(self):
        return f"Paciente {self.nome} ({self.especie}) - ID: {self.identidade}"
    # alterei nome (id para identidade)

    def __str__(self):
        return f"ID:{self.identidade:^6} | {self.nome:<18} - ({self.especie:^10} | Idade:{self.idade:^3}a | Peso:{self.peso:>5.2f}kg | Cadastrado:{str(self.cadastro):^6}"
    # retirei variáveis sobressalentes (raça, coloracao), alterei nome (id para identidade)



# o codigo original ta aqui embaixo.

# class Paciente:
#     def __init__(self, id_, nome, especie, raça, coloraçao, idade, peso, diagnostico, cadastro):
#         self.id = int(id_)
#         self.nome = nome
#         self.especie = especie  
#         self.raça = raça
#         self.coloraçao = coloraçao
#         self.idade = int(idade)
#         self.peso = float(peso)
#         self.diagnostico = diagnostico
#         self.cadastro = bool(cadastro) 

#     def para_linha(self):
#         return f"{self.id};{self.nome};{self.especie};{self.raça};{self.coloraçao};{self.idade};{self.peso};{self.diagnostico};{self.cadastro}\n"

#     def __repr__(self):
#         return f"Paciente {self.nome} ({self.especie}) - ID: {self.id}"

#     # Vai deixar a formatação mais bonitinha!
#     def __str__(self):
#         return f"ID:{self.id:^6} | {self.nome:<18} ({self.especie:^10} - {self.raça:<12}) | Cor:{self.coloraçao:^10} | Idade:{self.idade:^3}a | Peso:{self.peso:>5.2f}kg | Cadastrado:{str(self.cadastro):^6}" 
