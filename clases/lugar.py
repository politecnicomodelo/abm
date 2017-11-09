class Lugar(object):

    def __init__(self, codigo, nombre, coordenadas, tipo):

        self.codigo = codigo
        self.dependencias = []
        self.nombre = nombre
        self.coordenadas = coordenadas
        self.tipo = tipo



