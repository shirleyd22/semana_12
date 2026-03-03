#creamos la clase usuario
class Usuario:
    """
    esta clase representa un usuario de la biblioteca
    """
    def __init__(self, nombre, apellido, id_usuario):
        self.nombre = nombre
        self.apellido = apellido
        self.id_usuario = id_usuario
        #lista de libros prestados
        self._libros_prestados = []

    def get_nombre(self):
        return self.nombre
    def get_apellido(self):
        return self.apellido
    def get_id_usuario(self):
        return self.id_usuario
    def get_libros_prestados(self):
        return self._libros_prestados
    def prestar_libro(self, libro):
        self._libros_prestados.append(libro)
    def devolver_libro(self,codigo_libro):
        for libro in self._libros_prestados:
            if libro.get_codigo_libro() == codigo_libro:
                self._libros_prestados.remove(libro)
                return libro
        return None

    def __str__(self):
        return f"Usuario: {self._nombre} | ID: {self._id_usuario}"