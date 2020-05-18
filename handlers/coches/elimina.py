# coding: utf-8
#Eliminar comentario

import webapp2
import time

from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.coche import Coche

class EliminaCocheHandler(webapp2.RequestHandler):
    def get(self):
        coche = Coche.recupera(self.request)
        coche.key.delete()
        time.sleep(1)
        return self.redirect("/")


app = webapp2.WSGIApplication([
    ('/coches/elimina', EliminaCocheHandler)
], debug=True)
