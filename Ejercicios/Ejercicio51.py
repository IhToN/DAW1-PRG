"""
    Crear un diccionario cuya clave será un número de matrícula, y los datos del alumno serán una tupla de
    nombre, dirección, teléfono y email. En el sistema existen una serie de cursos, cada curso tendrá un
    identificador y una descripción del mismo. Necesitamos crear una estructura de enlace entre alumno y curso,
    de tal forma que sepamos qué alumnos están matriculados en cada curso.
    Será posible listar de forma interactiva los alumnos que hay en un curso específico.
"""

alumnos, cursos, matriculados = {}, {}, []


def add_alumno(dni, nombre, direccion, telefono, email):
    """ Agrega un alumno al listado de alumnos
    """
    alumnos[dni] = (nombre, direccion, telefono, email)


def add_curso(identificador, descripcion):
    """ Agrega un curso al listado de cursos
    """
    cursos[identificador] = descripcion


def matricular_alumno(id_curso, dni_alumno):
    """ Matricula a un alumno en el curso
    """
    matriculados.append((id_curso, dni_alumno))


def alumnos_de_curso(id_curso):
    """ Devuelve una lista con todos los alumnos matriculados
    en un curso
    """
    return [alumno for curso, alumno in matriculados if curso == id_curso]


add_alumno('10035214J', 'Pacman', 'El coño la Bernarda', '661352648', 'pacupacu@gmail.com')
add_curso('prog', 'Hala! A aprender Python, josdefruta!')
matricular_alumno('prog', '10035214J')
print(alumnos)
print(cursos)
print(matriculados)
print(alumnos_de_curso('prog'))
