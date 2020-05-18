# coding: utf-8
#Nueva marca

import webapp2
import time
from webapp2_extras import jinja2
from webapp2_extras.users import users
from google.appengine.ext import ndb

from model.marca import Marca
from model.coche import Coche


class NuevoCocheHandler(webapp2.RequestHandler):
    def get(self):

        jinja = jinja2.get_jinja2(app=self.app)

        valores_plantilla = {
            "clave_marca": self.request.GET["mar"]
        }

        self.response.write(jinja.render_template("nuevo_modelo.html", **valores_plantilla))

    def post(self):
        modelo = self.request.get("edModelo", "")
        str_ano = self.request .get("edAno", "")
        mecanicas = self.request.get("edMecanicas", "")
        fotonuevo = self.request.get("edFotoNuevo", "")
        fotousado = self.request.get("edFotoUsado", "")
        linknuevo = self.request.get("edLinkNuevo", "")
        linkusado = self.request.get("edLinkUsado", "")
        clave_marca = self.request.GET["mar"]

        try:
            ano = int(str_ano)
        except ValueError:
            ano = 0


        if(not(modelo) or not(ano) or not(mecanicas) or not(fotonuevo) or not(fotousado) or not(linknuevo) or not(linkusado)):
            return self.redirect("/")
        else:
            coche = Coche(modelo=modelo, mecanicas=mecanicas, ano=ano, fotonuevo=fotonuevo, fotousado=fotousado, linknuevo=linknuevo, linkusado=linkusado, clave_marca=ndb.Key(urlsafe=clave_marca))
            coche.put()
            time.sleep(1)
            return self.redirect("/coches/lista?mar=" + clave_marca)



app = webapp2.WSGIApplication([
    ('/coches/nuevo', NuevoCocheHandler)
], debug=True)
