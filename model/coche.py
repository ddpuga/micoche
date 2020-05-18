#Comentario introducido por un usuario

from google.appengine.ext import ndb

from marca import Marca

class Coche(ndb.Model):
    modelo = ndb.StringProperty(required=True)
    mecanicas = ndb.StringProperty()
    ano = ndb.IntegerProperty()
    fotonuevo = ndb.BlobProperty()
    fotousado = ndb.BlobProperty()
    linknuevo = ndb.StringProperty()
    linkusado = ndb.StringProperty()
    clave_marca = ndb.KeyProperty(kind=Marca)

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