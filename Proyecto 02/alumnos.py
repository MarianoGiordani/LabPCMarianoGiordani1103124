class ControlAlumnos:
    def __init__(self):
        # Iniciamos con algunos alumnos predeterminados para testeo
        self.alumnos = [
            {'carné': '2024001', 'nombre': 'Ana Torres', 'fecha_nacimiento': '2002-05-14'},
            {'carné': '2024002', 'nombre': 'Luis Gomez', 'fecha_nacimiento': '2001-08-19'},
            {'carné': '2024003', 'nombre': 'Sofía Paz', 'fecha_nacimiento': '2003-01-22'},
            {'carné': '2024004', 'nombre': 'Marco Jurado', 'fecha_nacimiento': '2004-07-03'}
        ]

    def agregar_alumno(self, carné, nombre, fecha_nacimiento):
        # Verificar que no exista otro alumno con el mismo carné
        if any(alumno['carné'] == carné for alumno in self.alumnos):
            print("Error: Ya existe un alumno con ese carné.")
        else:
            self.alumnos.append({
                'carné': carné,
                'nombre': nombre,
                'fecha_nacimiento': fecha_nacimiento
            })
            print("Alumno agregado exitosamente.")

    def editar_alumno(self, carné, nuevo_nombre=None, nueva_fecha_nacimiento=None):
        for alumno in self.alumnos:
            if alumno['carné'] == carné:
                if nuevo_nombre:
                    alumno['nombre'] = nuevo_nombre
                if nueva_fecha_nacimiento:
                    alumno['fecha_nacimiento'] = nueva_fecha_nacimiento
                print("Alumno actualizado exitosamente.")
                return
        print("Error: No se encontró un alumno con ese carné.")

    def listar_alumnos(self):
        if not self.alumnos:
            print("No hay alumnos registrados.")
        else:
            for alumno in self.alumnos:
                print(f"Carné: {alumno['carné']}, Nombre: {alumno['nombre']}, Fecha de nacimiento: {alumno['fecha_nacimiento']}")

