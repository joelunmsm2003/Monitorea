from mongoengine import *
from blog.settings import DBNAME
from django.contrib.auth.models import Group, User
from django.db import models

connect(DBNAME)

class Empresa(Document):
	id = models.AutoField(primary_key=True)
	name = StringField(max_length=120, required=True)

class User(Document):
	id = models.AutoField(primary_key=True)
	username = StringField(max_length=120, required=True)
	empresa = Empresa

class Equipos(Document):
	id = models.AutoField(primary_key=True)
	empresa = Empresa
	user = StringField(max_length=120)
	password = StringField(max_length=120)
	name = StringField(max_length=120)
	descripcion = StringField(max_length=120)
	ubicacion = StringField(max_length=120)
	empresa = StringField(max_length=120)

class Parametro(Document):
	id = models.AutoField(primary_key=True)
	ip = StringField(max_length=120)
	puerto_origen = StringField(max_length=120)
	puerto_final = StringField(max_length=120)
	equipo = Equipos
	tipo = StringField(max_length=120)

class Servicio(Document):
	id = Parametro
	servicio = StringField(max_length=120)
	user = StringField(max_length=120)
	password = StringField(max_length=120)
	puerto = StringField(max_length=120)