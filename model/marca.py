#Comentario introducido por un usuario

from google.appengine.ext import ndb

class Marca(ndb.Model):
    nombre = ndb.StringProperty()
    pais = ndb.StringProperty()
    foto = ndb.BlobProperty()

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()