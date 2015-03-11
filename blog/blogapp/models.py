from mongoengine import *
from blog.settings import DBNAME
from django.contrib.auth.models import Group, User
from django.db import models


connect(DBNAME)

class Empresa(Document):
	id = models.AutoField(primary_key=True)
	id_ticket = StringField(max_length=120)
	name = StringField(max_length=120, required=True)


class Equipos(Document):

	id = models.AutoField(primary_key=True)
	
	empresa = ReferenceField(Empresa, reverse_delete_rule=CASCADE)
	user = StringField(max_length=120)
	password = StringField(max_length=120)
	name = StringField(max_length=120)
	descripcion = StringField(max_length=120)
	ubicacion = StringField(max_length=120)


class Parametro(Document):
	
	id = models.AutoField(primary_key=True)
	ip = StringField(max_length=120)
	puerto_origen = StringField(max_length=120)
	puerto_final = StringField(max_length=120)
	equipo = ReferenceField(Equipos, reverse_delete_rule=CASCADE)
	tipo = StringField(max_length=120)
	servicio = StringField(max_length=120)
	user = StringField(max_length=120)
	password = StringField(max_length=120)



