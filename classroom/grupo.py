from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas else []
        if estudiantes:
            self.listadoAlumnos = self._ordenarAlumnos(estudiantes)
        else:
            self.listadoAlumnos = []

    def _ordenarAlumnos(self, estudiantes):
        orden_predefinido = ["Jaime", "David", "Oswaldo"]
        estudiantes_predefinidos = [alumno for alumno in estudiantes if alumno in orden_predefinido]
        estudiantes_ordenados = [alumno for alumno in estudiantes if alumno not in orden_predefinido]
        estudiantes_ordenados.sort()
        return estudiantes_predefinidos + estudiantes_ordenados

    def listadoAsignaturas(self, **kwargs):
        for nombre_asignatura in kwargs.values():
            self._asignaturas.append(Asignatura(nombre_asignatura, None))

    def agregarAlumno(self, alumno, otrosAlumnos=None):
        if isinstance(alumno, str):
            self.listadoAlumnos.append(alumno)
        if otrosAlumnos and isinstance(otrosAlumnos, list):
            self.listadoAlumnos.extend(otrosAlumnos)
        self.listadoAlumnos = self._ordenarAlumnos(self.listadoAlumnos)

    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}, Alumnos: {', '.join(self.listadoAlumnos)}"
