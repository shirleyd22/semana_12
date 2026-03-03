from modelos.libro import Libro
from modelos.usuario import Usuario

class BibliotecaServicio:
    """
    gestiona toda la logica del sistema de biblioteca
    """
    def __init__(self):
        #diccionario de libros :codigo del libro - > libro

        self._libros = {}
        #diccionario de usuarios : id -> usuario
        self._usuarios = {}
        #conjunto para controlar IDs unicos
        self._ids_usuarios = set()

        #libros

    def agregar_libro (self, titulo, autor, categoria, codigo_libro):
        if codigo_libro in self._libros:
            print("ya existe un libro con este codigo")
            return
        libro = Libro(titulo, autor, categoria, codigo_libro)
        self._libros[codigo_libro] = libro
        print("el libro fue agregado correctamente")

    def quitar_libro(self, codigo_libro):
        if codigo_libro in self._libros:
            del self._libros[codigo_libro]
            print("el libro fue eliminado correctamente")
        else:
            print("no existe el libro con ese codigo")

    #usuarios

    def registrar_usuario(self, nombre, apellido, id_usuario):
        if id_usuario in self._ids_usuarios:
            print("este id ya está registrado")
            return
        usuario = Usuario(nombre, apellido, id_usuario)
        self._usuarios[id_usuario] = usuario
        self._ids_usuarios.add(id_usuario)
        print("el usuario fue registrado correctamente")


    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self._usuarios:
            del self._usuarios[id_usuario]
            self._ids_usuarios.remove(id_usuario)
            print("usuario eliminado")
        else:
            print("usuario no encontrado")

    #prestamos

    def prestar_libro(self, codigo_libro, id_usuario):
        if codigo_libro not in self._libros:
            print("el libro no se encuentra disponible")
            return
        if id_usuario not in self._usuarios:
            print("el usuario no se encuentra registrado")
            return

        libro = self._libros.pop(codigo_libro)
        self._usuarios[id_usuario].prestar_libro(libro)
        print("el libro fue prestarado correctamente")

    def devolver_libro(self, codigo_libro, id_usuario):
        if id_usuario not in self._usuarios:
            print("el usuario no encontrado")
            return
        usuario = self._usuarios[id_usuario]
        libro = usuario.devolver_libro(codigo_libro)
        if libro:
            self._libros[codigo_libro] = libro
            print("el libro fue regresado correctamente")
        else:
            print("el usuario no tiene ese libro")

    #busqueda

    def buscar_por_titulo(self,titulo):
        for libro in self._libros.values():
            if libro.get_titulo_autor()[0].lower() == titulo.lower():
                print(libro)

    def buscar_por_autor(self, autor):
        for libro in self._libros.values():
            if libro.get_titulo_autor()[1].lower() == autor.lower():
                print(libro)

    def buscar_por_categoria(self, categoria):
        for libro in self._libros.values():
            if libro.get_categoria().lower() == categoria.lower():
                print(libro)

    #listado

    def listar_prestamo_usuario(self, id_usuario):
        if id_usuario not in self._usuarios:
            print("el usuario no fue encontado")
            return
        usuario = self._usuarios[id_usuario]
        print(f"\n libros prestados a { usuario.get_nombre()}: ")

        if not usuario.get_libros_prestados() :
            print("no tiene libros prestados")
            return

        for libro in usuario.get_libros():
            print(libro)
