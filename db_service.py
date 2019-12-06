"""
@autor Marco A. Gallegos
@date 2019/12/05
@descripcion aqui se implementan algunas funciones para probar en el servicio
"""

from models import *


def get_db_data():
    """Debe regresar un array de profesores"""
    prof = Profesor.select()
    return [profesor for profesor in prof]


if __name__ == "__main__":
    var = get_db_data()
    for prof in var:
        print(f"profesor {prof}")