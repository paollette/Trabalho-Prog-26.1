class Paciente:
    def __init__(self, id_, nome, especie, raça, coloraçao, idade, peso, diagnostico, cadastro):
        self.id = int(id_)
        self.nome = nome
        self.especie = especie  
        self.raça = raça
        self.coloraçao = coloraçao
        self.idade = int(idade)
        self.peso = float(peso)
        self.diagnostico = diagnostico
        self.cadastro = bool(cadastro) 

    def para_linha(self):
        return f"{self.id};{self.nome};{self.especie};{self.raça};{self.coloraçao};{self.idade};{self.peso};{self.diagnostico};{self.cadastro}\n"

    def __repr__(self):
        return f"Paciente {self.nome} ({self.especie}) - ID: {self.id}"

    # Vai deixar a formatação mais bonitinha!
    def __str__(self):
        return f"ID:{self.id:^6} | {self.nome:<18} ({self.especie:^10} - {self.raça:<12}) | Cor:{self.coloraçao:^10} | Idade:{self.idade:^3}a | Peso:{self.peso:>5.2f}kg | Cadastrado:{str(self.cadastro):^6}" 