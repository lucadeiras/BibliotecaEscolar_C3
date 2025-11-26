class Livro:
    def __init__(self, id_livro, genero, titulo, autor, editora, ano_publicacao, localizacao, num_paginas, estoque, disponivel):
        self.id_livro = id_livro
        self.genero = genero
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano_publicacao = ano_publicacao
        self.localizacao = localizacao
        self.num_paginas = num_paginas
        self.estoque = estoque
        self.disponivel = disponivel

    def get_id_livro(self):
        return self.id_livro

    def get_genero(self):
        return self.genero

    def get_titulo(self):
        return self.titulo

    def get_autor(self):
        return self.autor

    def get_editora(self):
        return self.editora

    def get_ano_publicacao(self):
        return self.ano_publicacao

    def get_localizacao(self):
        return self.localizacao

    def get_num_paginas(self):
        return self.num_paginas

    def get_estoque(self):
        return self.estoque

    def get_disponivel(self):
        return self.disponivel

    def set_id_livro(self, id_livro):
        self.id_livro = id_livro

    def set_genero(self, genero):
        self.genero = genero

    def set_titulo(self, titulo):
        self.titulo = titulo

    def set_autor(self, autor):
        self.autor = autor

    def set_editora(self, editora):
        self.editora = editora

    def set_ano_publicacao(self, ano_publicacao):
        self.ano_publicacao = ano_publicacao

    def set_localizacao(self, localizacao):
        self.localizacao = localizacao

    def set_num_paginas(self, num_paginas):
        self.num_paginas = num_paginas

    def set_estoque(self, estoque):
        self.estoque = estoque

    def set_disponivel(self, disponivel):
        self.disponivel = disponivel
   
    def to_string(self):
        return (
            f"Livro[ID={self.id_livro}, "
            f"Título={self.titulo}, "
            f"Autor={self.autor}, "
            f"Disponível={'Sim' if self.disponivel else 'Não'}]"
        )
