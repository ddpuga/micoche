# coding: utf-8
# Nueva marca

import webapp2
import time
from webapp2_extras import jinja2
from webapp2_extras.users import users
from model.marca import Marca


class NuevaMarcaHandler(webapp2.RequestHandler):
    def get(self):

        jinja = jinja2.get_jinja2(app=self.app)

        valores_plantilla = {
        }

        self.response.write(jinja.render_template("nueva_marca.html", **valores_plantilla))

    def post(self):
        nombre = self.request.get("edNombre", "")
        pais = self.request.get("edPais", "")
        foto = self.request.get("edFoto", "")

        if (not (nombre) or not (pais) or not (foto)):
            return self.redirect("/")
        else:
            marca = Marca(nombre=nombre, pais=pais, foto=foto)
            marca.put()
            time.sleep(1)
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/marcas/nueva', NuevaMarcaHandler)
], debug=True)
