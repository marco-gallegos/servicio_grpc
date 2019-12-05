from models import *

def get_db_data():
    prof = Profesor.select()
    return [profesor for profesor in prof]


if __name__ == "__main__":
    var = get_db_data()
    for prof in var:
        print(f"profesor {prof}")