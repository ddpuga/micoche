import webapp2
from google.appengine.ext import ndb


class ImageNuevo(webapp2.RequestHandler):
    def get(self):
        clave_coche = ndb.Key(urlsafe=self.request.get('edFotoNuevo'))
        coche = clave_coche.get()
        if coche.fotonuevo:
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(coche.fotonuevo)
        else:
            self.response.out.write('No image')

app = webapp2.WSGIApplication([
    ('/imgnuevo', ImageNuevo)
], debug=True)