#creamos la clase llamada Libro
class Libro:
    """
    esta representa un libro dentro del sistema de biblioteca
    """
    def __init__(self, titulo, autor, categoria, codigo_libro):
        #titulo y autor se almacenan como una tupla
        self._titulo_autor = (titulo, autor)
        self._categoria = categoria
        self._codigo_libro = codigo_libro
    #encapsulamiento con getters
    def get_titulo_autor(self):
        return self._titulo_autor
    def get_categoria(self):
        return self._categoria
    def get_codigo_libro(self):
        return self._codigo_libro
    def __str__(self):
        return f"ISBN: {self._codigo_libro} | {self._titulo_autor[0]} | {self._titulo_autor[1]} | {self._categoria}"