from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas if asignaturas else []
        self.listadoAlumnos = estudiantes if estudiantes else []

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x, None))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        if isinstance(alumno, str):
            self.listadoAlumnos.append(alumno)
        elif isinstance(alumno, list):
            self.listadoAlumnos.extend(alumno)

    def agregarGrupo(self, nombre_grupo, estudiantes):
        if isinstance(estudiantes, list):
            self._grupo = nombre_grupo
            self.listadoAlumnos.extend(estudiantes)
        else:
            print("La lista de estudiantes debe ser de tipo lista.")
    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}"
