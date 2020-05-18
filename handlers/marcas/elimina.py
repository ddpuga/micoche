# coding: utf-8
#Eliminar comentario

import webapp2
import time

from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.marca import Marca

class EliminaMarcaHandler(webapp2.RequestHandler):
    def get(self):
        marca = Marca.recupera(self.request)
        marca.key.delete()
        time.sleep(1)
        return self.redirect("/")

        #self.response.write(jinja.render_template("nuevo_comentario.html", **valores_plantilla))



app = webapp2.WSGIApplication([
    ('/marcas/elimina', EliminaMarcaHandler)
], debug=True)
