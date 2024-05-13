class ControlCursos:
    def __init__(self):
        # Inicialización con cursos predeterminados
        self.cursos = [
            {"id": "C001", "nombre": "Pensamiento Computacional", "horario": "Lunes 8:30 AM", "salon": "T-204", "catedratico": "Ing. Luis Ovalle"},
            {"id": "C002", "nombre": "Precalculo", "horario": "Miércoles 7:00 AM", "salon": "T-303", "catedratico": "Ing. Granja"},
            
        ]

    def crear_curso(self, id_curso, nombre, horario, salon, catedratico):
        # Verificar que el curso no exista ya
        if not any(curso['id'] == id_curso for curso in self.cursos):
            nuevo_curso = {
                "id": id_curso,
                "nombre": nombre,
                "horario": horario,
                "salon": salon,
                "catedratico": catedratico
            }
            self.cursos.append(nuevo_curso)
        else:
            print(f"Error: Ya existe un curso con el ID {id_curso}.")

    def editar_curso(self, id_curso, nombre, horario, salon, catedratico):
        for curso in self.cursos:
            if curso["id"] == id_curso:
                curso["nombre"] = nombre
                curso["horario"] = horario
                curso["salon"] = salon
                curso["catedratico"] = catedratico
                print("Curso actualizado exitosamente.")
                break
        else:
            print("Curso no encontrado.")

    def listar_cursos(self):
        print("Listado de Cursos:")
        for curso in self.cursos:
            print(f"ID: {curso['id']}, Nombre: {curso['nombre']}, Horario: {curso['horario']}, "
                  f"Salón: {curso['salon']}, Catedrático: {curso['catedratico']}")
