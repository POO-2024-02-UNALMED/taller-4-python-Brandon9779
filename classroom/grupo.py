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

    def agregarAlumno(self, alumno, *arg):
        if isinstance(alumno, str):
            self.listadoAlumnos.append(alumno)
        if arg:
            for estudiante in arg:
                if isinstance(estudiante, str):
                    self.listadoAlumnos.append(estudiante)
                elif isinstance(estudiante, list):
                    self.listadoAlumnos.extend(estudiante)

    def agregarGrupo(self, nombre_grupo, asignaturas=None, lista_alumnos=None):
        self._grupo = nombre_grupo
        if asignaturas:
          self._asignaturas.extend(asignaturas)
        if lista_alumnos:
          self.listadoAlumnos.extend(lista_alumnos)


    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}"
