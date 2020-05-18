# coding: utf-8

import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.coche import Coche
from model.marca import Marca
from model.comentario import Comentario
from google.appengine.ext import ndb


class ListaComentariosHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        coche, comentarios = Comentario.recupera_para(self.request)

        jinja = jinja2.get_jinja2(app=self.app)

        email = user.email()

        valores_plantilla = {
            "comentarios": comentarios,
            "coche": coche,
            "email": email
        }

        self.response.write(jinja.render_template("lista_comentarios.html", **valores_plantilla))

app = webapp2.WSGIApplication([
    ('/comentarios/lista', ListaComentariosHandler)
], debug=True)