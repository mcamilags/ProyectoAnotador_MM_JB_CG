class ErroresAnotador(Exception):
    pass

class ExisteLibro(ErroresAnotador):
    def __init__(self):
        self.msg : str

class NoExistePagina(ErroresAnotador):

    def __init__(self):
        self.msg: str

class ExisteSeccion(ErroresAnotador):
    def __init__(self):
        self.msg: str

class NoExisteNota(ErroresAnotador):
    def __init__(self):
        self.msg: str

class NoExisteNotaDestacada(ErroresAnotador):

    def __init__(self):
        self.msg: str
class NoExisteEtiqueta(ErroresAnotador):

    def __init__(self):
        self.msg: str

class NotaNoEncontrada(ErroresAnotador):
    def __init__(self):
        self.msg: str

class FechaNoEncontrada(ErroresAnotador):
    def __init__(self):
        self.msg: str

class NoExisteNombreEtiqueta(ErroresAnotador):
    def __init__(self):
        self.msg: str

