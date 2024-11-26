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

    def agregarAlumno(self, alumno, *args):
        if isinstance(alumno, str):
            self.listadoAlumnos.append(alumno)
        for extra_alumnos in args:
            if isinstance(extra_alumnos, list):
                self.listadoAlumnos.extend(extra_alumnos)

    def agregarAlumno(self, alumno, otrosAlumnos=None):
        self.listadoAlumnos.append(alumno)
        if otrosAlumnos:
            self.listadoAlumnos.extend(otrosAlumnos)
    
    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}"

