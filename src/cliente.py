from datetime import datetime
now = datetime.now()

class Cliente:
    def __init__(self, nome, cpf_number, ano_nascimento):
        self.nome = nome
        self.cpf_number = cpf_number
        self.idade = now.year - ano_nascimento
        self.ano_nascimento = ano_nascimento
