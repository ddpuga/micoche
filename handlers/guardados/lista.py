# coding: utf-8

import webapp2
from webapp2_extras import jinja2

from model.guardado import Guardado
from webapp2_extras.users import users
from model.coche import Coche



class ListaGuardadosHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()

        if usr:
            listaguardados = []
            coches = []
            guardados = Guardado.query(Guardado.email == usr.email())
            for guardado in guardados:
                listaguardados.append(guardado.clave_coche)

            for guardado in guardados:
                coches.append(Coche.get_by_id(guardado.clave_coche))

            jinja = jinja2.get_jinja2(app=self.app)

            valores_plantilla = {
                "guardados": listaguardados,
                "coches": coches
            }

            self.response.write(jinja.render_template("lista_guardados.html", **valores_plantilla))
        else:
            self.redirect("/")
app = webapp2.WSGIApplication([
    ('/guardados/lista', ListaGuardadosHandler)
], debug=True)