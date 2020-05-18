# coding: utf-8
# Nuevo comentario

import webapp2
import time
from webapp2_extras import jinja2
from webapp2_extras.users import users
from google.appengine.ext import ndb

from model.guardado import Guardado


class NuevoGuardadoHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()

        clave_coche = Guardado.recupera(self.request)

        guardado = Guardado(email=usr.email(), clave_coche=clave_coche.key.id())
        guardado.put()
        time.sleep(1)
        return self.redirect("/guardados/lista")


app = webapp2.WSGIApplication([
    ('/guardados/nuevo', NuevoGuardadoHandler)
], debug=True)
