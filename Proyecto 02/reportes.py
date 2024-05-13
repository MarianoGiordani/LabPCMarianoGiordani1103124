class ModuloReportes:
    def __init__(self, cursos, alumnos, calificaciones):
        self.cursos = cursos
        self.alumnos = alumnos
        self.calificaciones = calificaciones

    def reporte_cantidad_estudiantes(self):
        print("Reporte de cantidad de estudiantes por curso:")
        curso_estudiantes = {curso['id']: 0 for curso in self.cursos}
        for calificacion in self.calificaciones:
            if calificacion['id_curso'] in curso_estudiantes:
                curso_estudiantes[calificacion['id_curso']] += 1
        for curso_id, count in sorted(curso_estudiantes.items(), key=lambda item: item[1], reverse=True):
            curso_nombre = next((curso['nombre'] for curso in self.cursos if curso['id'] == curso_id), "Curso Desconocido")
            print(f"Curso: {curso_nombre}, Estudiantes: {count}")

    def reporte_estudiantes_por_curso(self, id_curso):
        print(f"Estudiantes en el curso ID {id_curso}:")
        estudiantes_en_curso = [cal for cal in self.calificaciones if cal['id_curso'] == id_curso]
        for est in estudiantes_en_curso:
            estudiante = next((alumno for alumno in self.alumnos if alumno['carne'] == est['carnet']), None)
            if estudiante:
                print(f"{estudiante['nombre']} - Nota: {est['nota']}")

    def reporte_notas_por_estudiante(self, carnet):
        print(f"Notas para el estudiante con carné {carnet}:")
        notas = [cal for cal in self.calificaciones if cal['carnet'] == carnet]
        for nota in notas:
            curso = next((curso for curso in self.cursos if curso['id'] == nota['id_curso']), None)
            if curso:
                print(f"Curso: {curso['nombre']} - Nota: {nota['nota']}")

    def reporte_promedio_notas_por_curso(self):
        print("Promedio de notas por curso:")
        curso_notas = {curso['id']: [] for curso in self.cursos}
        for calificacion in self.calificaciones:
            curso_notas[calificacion['id_curso']].append(calificacion['nota'])
        for curso_id, notas in curso_notas.items():
            if notas:
                promedio = sum(notas) / len(notas)
                curso_nombre = next((curso['nombre'] for curso in self.cursos if curso['id'] == curso_id), "Curso Desconocido")
                print(f"Curso: {curso_nombre} - Promedio: {promedio:.2f}")

    def reporte_mejor_estudiante(self):
        print("Estudiante con mejor desempeño general:")
        estudiante_promedios = {}
        for calificacion in self.calificaciones:
            if calificacion['carnet'] in estudiante_promedios:
                estudiante_promedios[calificacion['carnet']].append(calificacion['nota'])
            else:
                estudiante_promedios[calificacion['carnet']] = [calificacion['nota']]
        mejor_promedio = None
        mejor_estudiante = None
        for carnet, notas in estudiante_promedios.items():
            promedio = sum(notas) / len(notas)
            if mejor_promedio is None or promedio > mejor_promedio:
                mejor_promedio = promedio
                mejor_estudiante = next((alumno for alumno in self.alumnos if alumno['carne'] == carnet), None)
        if mejor_estudiante:
            print(f"{mejor_estudiante['nombre']} - Promedio: {mejor_promedio:.2f}")

# Prueba básica para asegurar que el módulo funciona correctamente
if __name__ == "__main__":
    cursos = [{'id': 1, 'nombre': 'Matemáticas'}, {'id': 2, 'nombre': 'Historia'}]
    alumnos = [{'carne': '2020001', 'nombre': 'Juan Perez'}, {'carne': '2020002', 'nombre': 'Ana Gomez'}]
    calificaciones = [{'carnet': '2020001', 'id_curso': 1, 'nota': 85}, {'carnet': '2020002', 'id_curso': 2, 'nota': 90}]
    modulo_reportes = ModuloReportes(cursos, alumnos, calificaciones)
    modulo_reportes.reporte_cantidad_estudiantes()
