#Comentario introducido por un usuario

from google.appengine.ext import ndb

class Usuario(ndb.Model):
    nombre = ndb.StringProperty()
    email = ndb.StringProperty()
    coches = ndb.StringProperty()