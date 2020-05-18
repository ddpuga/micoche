# coding: utf-8

import webapp2
from webapp2_extras import jinja2

from model.coche import Coche
from model.marca import Marca

class ListaCochesHandler(webapp2.RequestHandler):
    def get(self):
        marca, coches = Coche.recupera_para(self.request)

        jinja = jinja2.get_jinja2(app=self.app)

        valores_plantilla = {
            "coches": coches,
            "marca": marca
        }

        self.response.write(jinja.render_template("lista_modelos.html", **valores_plantilla))



app = webapp2.WSGIApplication([
    ('/coches/lista', ListaCochesHandler)
], debug=True)
