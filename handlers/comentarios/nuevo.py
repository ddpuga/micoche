# coding: utf-8
#Nuevo comentario

import webapp2
import time
from webapp2_extras import jinja2
from webapp2_extras.users import users
from google.appengine.ext import ndb

from model.comentario import Comentario


class NuevoComentarioHandler(webapp2.RequestHandler):
    def get(self):

        jinja = jinja2.get_jinja2(app=self.app)

        valores_plantilla = {
            "clave_coche": self.request.GET["coc"]
        }

        self.response.write(jinja.render_template("nuevo_comentario.html", **valores_plantilla))

    def post(self):
        usr = users.get_current_user()

        tipo = self.request.get("edTipo", "")
        mensaje = self.request.get("edMensaje", "")
        clave_coche = self.request.GET["coc"]

        if(not(tipo) or not(mensaje)):
            return self.redirect("/")
        else:
            comentario = Comentario(mensaje=mensaje, tipo=tipo, email=usr.email(), clave_coche=ndb.Key(urlsafe=clave_coche))
            comentario.put()
            time.sleep(1)
            return self.redirect("/comentarios/lista?coc=" + clave_coche)



app = webapp2.WSGIApplication([
    ('/comentarios/nuevo', NuevoComentarioHandler)
], debug=True)
