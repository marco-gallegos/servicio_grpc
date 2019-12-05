import peewee as pwe

psql_db = pwe.PostgresqlDatabase(database='necronomicon', user="postgres", password="postgres", host="localhost")


class Alumno(pwe.Model):
    class Meta:
        database = psql_db
        table_name = 'alumnos'

    id_alumno = pwe.AutoField()
    nombre = pwe.CharField(max_length=100, null=False)
    email = pwe.CharField(max_length=100, null=False)
    tutor = pwe.DeferredForeignKey(rel_model_name="Profesor", column_name="tutor", backref="alumnos" )


deferred_alumno_clase = pwe.DeferredThroughModel()


class Clase(pwe.Model):
    class Meta:
        database = psql_db
        table_name = 'clases'

    id_clase = pwe.AutoField()
    nombre = pwe.CharField(max_length=100, null=False)
    horario = pwe.CharField(max_length=100, null=False)
    alumnos = pwe.ManyToManyField(model=Alumno, backref="clases", through_model=deferred_alumno_clase)


class AlumnoClase(pwe.Model):
    class Meta:
        database = psql_db
        table_name = 'alumno_clase'
    id_alumno_clase = pwe.AutoField()
    id_alumno = pwe.ForeignKeyField(model=Alumno, column_name="id_alumno")
    id_clase = pwe.ForeignKeyField(model=Clase, column_name="id_clase")


# resolvemos el modelo deferido
deferred_alumno_clase.set_model(AlumnoClase)


# AlumnoClase = Clase.alumnos.get_through_model()
class Profesor(pwe.Model):
    class Meta:
        database = psql_db
        table_name = 'profesores'

    id_profesor = pwe.AutoField()
    nombre = pwe.CharField(max_length=100, null=False)
    especialidad = pwe.CharField(max_length=100, null=False)
    titulo = pwe.CharField(max_length=100, null=False)
