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

    def agregarGrupo(self, grupo, asignaturas=None, alumnos=None, *arg):
        self._grupo = grupo
        if asignaturas:
           self._asignaturas.extend(asignaturas)
        if alumnos:
           if isinstance(alumnos, list):
               self.listadoAlumnos.extend(alumnos)
           elif isinstance(alumnos, str):
               self.listadoAlumnos.append(alumnos)
        for extra_alumnos in arg:
            if isinstance(extra_alumnos, list):
               self.listadoAlumnos.extend(extra_alumnos)
            elif isinstance(extra_alumnos, str):
               self.listadoAlumnos.append(extra_alumnos)


    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}"
