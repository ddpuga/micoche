#Coche guardado por un usuario

from google.appengine.ext import ndb

from marca import Marca
from coche import Coche

class Guardado(ndb.Model):
    clave_coche = ndb.IntegerProperty(required=True, indexed=True)
    email = ndb.StringProperty(required=True, indexed=True)

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()

    @staticmethod
    def recupera_para(req):
        try:
            id_mar = req.GET["mar"]
        except KeyError:
            id_mar = ""

        if id_mar:
            clave_marca = ndb.Key(urlsafe=id_mar)
            coches = Coche.query(Coche.clave_marca == clave_marca)
            return (clave_marca.get(), coches)
        else:
            print("ERROR: marca no encontrada")

    @staticmethod
    def recupera_usuario(req):
        try:
            email = req
        except KeyError:
            email = ""

        if email:
            guardados = Guardado.query(Guardado.email == email)
            coches = Coche.query(Coche.key)
            return (guardados)
        else:
            print("ERROR: marca no encontrada")