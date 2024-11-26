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
            self.listadoAlumnos.extend(arg)

    def agregarGrupo(self, nombre_grupo, *arg):
        self._grupo = nombre_grupo
        for estudiantes in arg:
            if isinstance(estudiantes, list):  
                self.listadoAlumnos.extend(estudiantes)
            elif isinstance(estudiantes, str): 
                self.listadoAlumnos.append(estudiantes)
            else:
                print("Error: El argumento debe ser una lista de estudiantes o un solo estudiante.")
    
    @classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}"
