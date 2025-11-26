from .aluno import Aluno
from .livro import Livro

class Emprestimo:
    def __init__(self, id_emprestimo, aluno, livro, data_emprestimo, data_devolucao, atraso=False, multa=0.0, emprestado=True):
        self.id_emprestimo = id_emprestimo
        self.aluno = aluno        
        self.livro = livro        
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.atraso = atraso
        self.multa = multa
        self.emprestado = emprestado
   
    # ---------- GETTERS e SETTERS ----------
    def get_id_emprestimo(self):
        return self.id_emprestimo
    def set_id_emprestimo(self, id_emprestimo):
        self.id_emprestimo = id_emprestimo

    def get_aluno(self):
        return self.aluno
    def set_aluno(self, aluno):
        self.aluno = aluno

    def get_livro(self):
        return self.livro
    def set_livro(self, livro):
        self.livro = livro

    def get_data_emprestimo(self):
        return self.data_emprestimo
    def set_data_emprestimo(self, data_emprestimo):
        self.data_emprestimo = data_emprestimo

    def get_data_devolucao(self):
        return self.data_devolucao
    def set_data_devolucao(self, data_devolucao):
        self.data_devolucao = data_devolucao

    def get_atraso(self):
        return self.atraso
    def set_atraso(self, atraso):
        self.atraso = atraso

    def get_multa(self):
        return self.multa
    def set_multa(self, multa):
        self.multa = multa

    def get_emprestado(self):
        return self.emprestado
    def set_emprestado(self, emprestado):
        self.emprestado = emprestado

    # ---------- REPRESENTAÇÃO ----------
    def to_string(self):
        return (
            f"Empréstimo[ID={self.id_emprestimo}, "
            f"Aluno={self.aluno.get_nome()}, "
            f"Livro={self.livro.get_titulo()}, "
            f"Data Empréstimo={self.data_emprestimo}, "
            f"Devolução={self.data_devolucao}, "
            f"Multa={self.multa}]"
        )
