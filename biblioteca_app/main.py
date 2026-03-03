from servicios.biblioteca_servicio import  BibliotecaServicio

def mostrar_menu():
    print("\n Bienvenido al sistema de la biblioteca digital")
    print("\n a continuacion se mostraran las opciones: ")
    print("1. agregar libro")
    print("2. quitar libro")
    print("3. registrar usuario")
    print("4. dar de baja a un usuario")
    print("5. prestar libro")
    print("6. devolver libro")
    print("7. buscar libro por titulo")
    print("8. buscar libro por autor")
    print("9. buscar libro por categoría")
    print("10. listar libros prestados")
    print("0. salir")

def main():
    biblioteca = BibliotecaServicio()
    while True:
        mostrar_menu()
        opcion = input("Escribe una opcion: ")

        if opcion == "1":
            titulo = input("Ingrese tu titulo: ")
            autor = input("Ingrese tu autor: ")
            categoria = input("Ingrese tu categoria: ")
            codigo_libro = input("Ingrese tu codigo_libro: ")
            biblioteca.agregar_libro(titulo, autor, categoria, codigo_libro)

        elif opcion == "2":
            codigo_libro = input("ingrese el codigo del libro: ")
            biblioteca.quitar_libro(codigo_libro)

        elif opcion == "3":
            nombre = input("Ingrese tu nombre: ")
            apellido = input("Ingrese tu apellido: ")
            id_usuario = input("Ingrese tu id_usuario: ")
            biblioteca.registrar_usuario(nombre, apellido, id_usuario)

        elif opcion == "4":
            id_usuario = input("id del usuario: ")
            biblioteca.dar_baja_usuario(id_usuario)

        elif opcion == "5":
            codigo_libro = input("codigo del libro")
            id_usuario = input("id del usuario")
            biblioteca.prestar_libro(codigo_libro, id_usuario)

        elif opcion == "6":
            codigo_libro = input("codigo del libro: ")
            id_usuario = input("id del usuario: ")
            biblioteca.devolver_libro(codigo_libro, id_usuario)

        elif opcion == "7":
            titulo = input("Ingrese tu titulo: ")
            biblioteca.buscar_por_titulo(titulo)

        elif opcion == "8":
            autor = input("Ingrese tu autor: ")
            biblioteca.buscar_por_autor(autor)

        elif opcion == "9":
            categoria = input("categoria: ")
            biblioteca.buscar_por_categoria(categoria)

        elif opcion == "10":
            id_usuario = input("id del usuario: ")
            biblioteca.listar_prestamo_usuario(id_usuario)

        elif opcion == "0":
            print("saliendo del sistema")
            break

        else:
            print("Opcion no valida")

if __name__ == "__main__":
    main()