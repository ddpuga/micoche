#Comentario introducido por un usuario

from google.appengine.ext import ndb
from coche import Coche

class Comentario(ndb.Model):
    hora = ndb.DateTimeProperty(auto_now_add=True, indexed=True)
    email = ndb.StringProperty()
    tipo = ndb.StringProperty()
    mensaje = ndb.StringProperty()
    clave_coche = ndb.KeyProperty(kind=Coche)

    @staticmethod
    def recupera_para(req):
        try:
            id_coc = req.GET["coc"]
        except KeyError:
            id_coc = ""

        if id_coc:
            clave_coche = ndb.Key(urlsafe=id_coc)
            comentarios = Comentario.query(Comentario.clave_coche == clave_coche)
            return (clave_coche.get(), comentarios)
        else:
            print("ERROR: coche no encontrado")

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()
