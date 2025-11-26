class Aluno:
    def __init__(self, matricula, nome, cpf, email, telefone, endereco, turma, data_nascimento):
        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone
        self.endereco = endereco
        self.turma = turma
        self.data_nascimento = data_nascimento

    # ==========================
    # Getters e Setters
    # ==========================

    def get_matricula(self):
        return self.matricula

    def set_matricula(self, matricula):
        self.matricula = matricula

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_cpf(self):                     # ✅ Faltava este método
        return self.cpf

    def set_cpf(self, cpf):
        self.cpf = cpf

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_telefone(self):
        return self.telefone

    def set_telefone(self, telefone):
        self.telefone = telefone

    def get_endereco(self):
        return self.endereco

    def set_endereco(self, endereco):
        self.endereco = endereco

    def get_turma(self):
        return self.turma

    def set_turma(self, turma):
        self.turma = turma

    def get_data_nascimento(self):
        return self.data_nascimento

    def set_data_nascimento(self, data_nascimento):
        self.data_nascimento = data_nascimento

    # ==========================
    # Representação em texto
    # ==========================
    def to_string(self):
        return f"Aluno[Matrícula={self.matricula}, Nome={self.nome}, Turma={self.turma}]"
