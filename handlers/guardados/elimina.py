# coding: utf-8
# Eliminar comentario

import webapp2
import time

from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.guardado import Guardado
from model.coche import Coche


class EliminaGuardadoHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            coche = Coche.recupera(self.request)
            guardados = Guardado.query(Guardado.email == user.email(), Guardado.clave_coche == coche.key.id())
            for g in guardados:
                g.key.delete()
            time.sleep(1)
            return self.redirect("/guardados/lista")
        else:
            return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/guardados/elimina', EliminaGuardadoHandler)
], debug=True)
