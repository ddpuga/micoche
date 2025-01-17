#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from webapp2_extras import jinja2
from webapp2_extras.users import users

from model.comentario import Comentario

def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

class RespuestaHandler(webapp2.RequestHandler):

    def get(self):

            comentarios = Comentario.query().order(Comentario.hora)

            jinja = jinja2.get_jinja2(app=self.app)

            valores_plantilla = {
                "comentarios": comentarios
            }

            self.response.write(jinja.render_template("answer.html", **valores_plantilla))

app = webapp2.WSGIApplication([
    ('/hello', RespuestaHandler)
], debug=True)
