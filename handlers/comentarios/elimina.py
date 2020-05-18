# coding: utf-8
#Eliminar comentario

import webapp2
import time

from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.comentario import Comentario


class EliminaComentarioHandler(webapp2.RequestHandler):
    def get(self):
        comentario = Comentario.recupera(self.request)
        clave_coche = self.request.GET["coc"]
        comentario.key.delete()
        time.sleep(1)
        return self.redirect("/comentarios/lista?coc=" + clave_coche)

        #self.response.write(jinja.render_template("nuevo_comentario.html", **valores_plantilla))



app = webapp2.WSGIApplication([
    ('/comentarios/elimina', EliminaComentarioHandler)
], debug=True)
