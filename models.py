class Restaurante:
    def __init__(self, id, nome, imagem, endereco, horario, especialista):
        self.__id = id
        self.__nome = nome
        self.__imagem = imagem
        self.__endereco = endereco
        self.__horario = horario
        self.__especialista = especialista

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_imagem(self):
        return self.__imagem

    def get_endereco(self):
        return self.__endereco

    def get_horario(self):
        return self.__horario

    def get_especialista(self):
        return self.__especialista


class Especialista:
    def __init__(self, nome, comentario):
        self.__nome = nome
        self.__comentario = comentario

    def get_nome(self):
        return self.__nome

    def get_comentario(self):
        return self.__comentario
