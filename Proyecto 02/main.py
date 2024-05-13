#Importar Funciones de los Modulos 
from cursos import ControlCursos
from alumnos import ControlAlumnos
from calificaciones import ControlCalificaciones
from reportes import ModuloReportes

def main():
    # Inicializamos los controles para cursos, alumnos, calificaciones y reportes
    control_cursos = ControlCursos()
    control_alumnos = ControlAlumnos()
    control_calificaciones = ControlCalificaciones()
    modulo_reportes = ModuloReportes(control_cursos, control_alumnos, control_calificaciones)

    # Bucle interactivo para el menú principal
    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestión de Cursos")
        print("2. Gestión de Alumnos")
        print("3. Calificaciones")
        print("4. Reportes")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            # Submenú para gestión de cursos
            while True:
                print("\n--- Gestión de Cursos ---")
                print("a. Crear Curso")
                print("b. Editar Curso")
                print("c. Listar Cursos")
                print("d. Volver al Menú Principal")
                opcion_cursos = input("Seleccione una opción (a-d): ")

                if opcion_cursos == "a":
                    id_curso = input("Ingrese el ID del curso: ")
                    nombre = input("Ingrese el nombre del curso: ")
                    horario = input("Ingrese el horario del curso: ")
                    salon = input("Ingrese el salón del curso: ")
                    catedratico = input("Ingrese el nombre del catedrático: ")
                    control_cursos.crear_curso(id_curso, nombre, horario, salon, catedratico)

                elif opcion_cursos == "b":
                    control_cursos.listar_cursos()
                    id_curso = input("Ingrese el ID del curso que desea editar: ")
                    nombre = input("Ingrese el nuevo nombre del curso: ")
                    horario = input("Ingrese el nuevo horario del curso: ")
                    salon = input("Ingrese el nuevo salón del curso: ")
                    catedratico = input("Ingrese el nuevo nombre del catedrático: ")
                    control_cursos.editar_curso(id_curso, nombre, horario, salon, catedratico)

                elif opcion_cursos == "c":
                    control_cursos.listar_cursos()

                elif opcion_cursos == "d":
                    break

                else:
                    print("Opción no válida. Intente nuevamente.")

        elif opcion == "2":
            # Submenú para gestión de alumnos
            while True:
                print("\n--- Gestión de Alumnos ---")
                print("a. Crear Alumno")
                print("b. Editar Alumno")
                print("c. Listar Alumnos")
                print("d. Volver al Menú Principal")
                opcion_alumnos = input("Seleccione una opción (a-d): ")

                if opcion_alumnos == "a":
                    carne = input("Ingrese el carné del alumno: ")
                    nombre = input("Ingrese el nombre del alumno: ")
                    fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno (YYYY-MM-DD): ")
                    control_alumnos.crear_alumno(carne, nombre, fecha_nacimiento)

                elif opcion_alumnos == "b":
                    control_alumnos.listar_alumnos()
                    carne = input("Ingrese el carné del alumno que desea editar: ")
                    nombre = input("Ingrese el nuevo nombre del alumno: ")
                    fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento del alumno (YYYY-MM-DD): ")
                    control_alumnos.editar_alumno(carne, nombre, fecha_nacimiento)

                elif opcion_alumnos == "c":
                    control_alumnos.listar_alumnos()

                elif opcion_alumnos == "d":
                    break

                else:
                    print("Opción no válida. Intente nuevamente.")

        elif opcion == "3":
            # Módulo de calificaciones
            while True:
                print("\n--- Módulo de Calificaciones ---")
                print("a. Asignar Nota a Alumno")
                print("b. Obtener Notas de Curso")
                print("c. Obtener Notas de Alumno")
                print("d. Volver al Menú Principal")
                opcion_calificaciones = input("Seleccione una opción (a-d): ")

                if opcion_calificaciones == "a":
                    id_curso = input("Ingrese el ID del curso: ")
                    carnet_alumno = input("Ingrese el carné del alumno: ")
                    nota = float(input("Ingrese la nota a asignar: "))
                    control_calificaciones.asignar_nota(id_curso, carnet_alumno, nota)

                elif opcion_calificaciones == "b":
                    id_curso = input("Ingrese el ID del curso para obtener las notas: ")
                    control_calificaciones.obtener_notas_curso(id_curso)

                elif opcion_calificaciones == "c":
                    carnet_alumno = input("Ingrese el carné del alumno para obtener las notas: ")
                    control_calificaciones.obtener_notas_alumno(carnet_alumno)

                elif opcion_calificaciones == "d":
                    break

                else:
                    print("Opción no válida. Intente nuevamente.")

        elif opcion == "4":
            # Submenú para reportes
            modulo_reportes.menu_reportes()

        elif opcion == "5":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
