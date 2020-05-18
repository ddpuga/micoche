import webapp2
from google.appengine.ext import ndb


class ImageUsado(webapp2.RequestHandler):
    def get(self):
        clave_coche = ndb.Key(urlsafe=self.request.get('edFotoUsado'))
        coche = clave_coche.get()
        if coche.fotousado:
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(coche.fotousado)
        else:
            self.response.out.write('No image')

app = webapp2.WSGIApplication([
    ('/imgusado', ImageUsado)
], debug=True)