from classroom.asignatura import Asignatura

class Grupo:
    grado = None

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=[]):
        lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + lista

    def agregarAlumno(self, *alumnos):
        for alumno in alumnos:
            if isinstance(alumno, list):
                self.listadoAlumnos.extend(alumno)
            else:
                self.listadoAlumnos.append(alumno)

    def listadoAsignaturas(self, **asignaturas):
        for nombre_asignatura in asignaturas.values():
            self._asignaturas.append(Asignatura(nombre_asignatura))

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}"

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre
