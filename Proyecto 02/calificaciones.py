class ControlCalificaciones:
    def __init__(self):
        self.calificaciones = {}

    def asignar_nota(self, carnet_alumno, nota):
        id_curso = input("Ingrese el ID del curso: ")
        if id_curso not in self.calificaciones:
            self.calificaciones[id_curso] = {}

        if carnet_alumno not in self.calificaciones[id_curso]:
            self.calificaciones[id_curso][carnet_alumno] = nota
            print(f"Nota asignada correctamente para el alumno con carné {carnet_alumno} en el curso {id_curso}.")
        else:
            print(f"El alumno con carné {carnet_alumno} ya tiene una nota asignada en el curso {id_curso}.")

    def obtener_notas_curso(self, id_curso):
        if id_curso in self.calificaciones:
            print(f"Notas del curso con ID {id_curso}:")
            for carné, nota in self.calificaciones[id_curso].items():
                print(f"Carné: {carné}, Nota: {nota}")
        else:
            print(f"No se encontraron notas para el curso con ID {id_curso}.")

    def obtener_notas_alumno(self, carnet_alumno):
        print(f"Notas del alumno con carné {carnet_alumno}:")
        encontrado = False
        for id_curso, notas in self.calificaciones.items():
            if carnet_alumno in notas:
                print(f"Curso ID: {id_curso}, Nota: {notas[carnet_alumno]}")
                encontrado = True
        if not encontrado:
            print("El alumno no tiene notas registradas en ningún curso.")
