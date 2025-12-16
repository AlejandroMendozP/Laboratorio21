class Libro:
    def __init__(self, titulo, autor, año, disponible):
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.disponibilidad = disponible

    def prestarse_libro(self):
        if (self.disponibilidad == True):
            print("Libro prestado")
            self.disponibilidad = False
        else:
            print("Libro no disponible")
    
    def devolver_libro(self):
        if (self.disponibilidad == False):
            print("Libro devuelto")
            self.disponibilidad = True
        else:
            print("Libro ya devuelto")
    
class LibroDigital(Libro):
    def __init__(self, titulo, autor, año, disponible, formato, tamañoMB):
        super().__init__(titulo, autor, año, disponible)
        self.formato = formato
        self.tamañoMB = tamañoMB
    
    def prestarse_libro(self):
            print("Libro prestado")
            self.disponibilidad = True

class Biblioteca:

    def __init__(self):
        self.libros = []

    def agregar_libro(self):
        opcion = int(input("1.Libro físico\n2.Libro Digital\n"))
        match (opcion):
            case 1:
                titulo = input("Ingrese el titulo: ")
                autor = input("Ingrese el autor: ")
                año = int(input("Ingrese el año: "))
                disponible = True
                libro = Libro(titulo, autor, año, disponible)
                self.libros.append(libro)
            case 2:
                titulo = input("Ingrese el titulo: ")
                autor = input("Ingrese el autor: ")
                año = int(input("Ingrese el año: "))
                disponible = True
                formato = input("Ingrese el formato: ")
                tamaño = input("Ingrese el tamaño MB: ")
                libro = LibroDigital(titulo, autor, año, disponible, formato, tamaño)
                self.libros.append(libro)
    
    def listar_libros(self):
        for libro in self.libros:
            if isinstance(libro, LibroDigital):
                print(f"Titulo: {libro.titulo}\nAutor: {libro.autor}\nAño de publicacion: {libro.año}\nDisponible: {libro.disponibilidad}")
                print(f"Formato: {libro.formato}\nTamaño: {libro.tamañoMB}")
            elif isinstance(libro, Libro):
                print(f"Titulo: {libro.titulo}\nAutor: {libro.autor}\nAño de publicacion: {libro.año}\nDisponible: {libro.disponibilidad}")
        
    def buscar_autor(self, autor):
        for libro in self.libros:
            if (autor == libro.autor):
                return libro
        return None
    
    def mostrar_libro(self, libro):
        if isinstance(libro, LibroDigital):
            print(f"Titulo: {libro.titulo}\nAutor: {libro.autor}\nAño de publicacion: {libro.año}\nDisponible: {libro.disponibilidad}")
            print(f"Formato: {libro.formato}\nTamaño: {libro.tamañoMB}")
        elif isinstance(libro, Libro):
            print(f"Titulo: {libro.titulo}\nAutor: {libro.autor}\nAño de publicacion: {libro.año}\nDisponible: {libro.disponibilidad}")

    def prestar_libro(self, autor):
        libro = self.buscar_autor(autor)
        if (libro == None):
            print("Libro no encontrado")
        libro.prestarse_libro()
    
    def devolver_libro(self, autor):
        libro = self.buscar_autor(autor)
        if (libro == None):
            print("Libro no encontrado")
        libro.devolver_libro()


biblio = Biblioteca()

print("Bienvenido al sistema de Biblioteca")
while True:
    print("1.Añadir libro\n2.Prestar libro\n3.Devolver Libro\n4.Buscar libro por autor\n5.Listar libros\n6. Salir")
    opcion = int(input("Seleccione una opcion: "))
    match (opcion):
        case 1:
            biblio.agregar_libro()
        case 2:
            autor = input("Ingrese el autor: ")
            biblio.prestar_libro(autor)
        case 3:
            autor = input("Ingrese el autor: ")
            biblio.devolver_libro(autor)
        case 4:
            autor = input("Ingrese el autor: ")
            libro = biblio.buscar_autor(autor)
            if (libro != None):
                biblio.mostrar_libro(libro)
            else:
                print("Libro no encontrado")
        case 5:
            biblio.listar_libros()
        case 6:
            print("Gracias por usar la Biblioteca")
            break
        case _:
            print("Opcion no valida")