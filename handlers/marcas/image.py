import webapp2
from google.appengine.ext import ndb


class Image(webapp2.RequestHandler):
    def get(self):
        clave_marca = ndb.Key(urlsafe=self.request.get('edFoto'))
        marca = clave_marca.get()
        if marca.foto:
            self.response.headers['Content-Type'] = 'image/png'
            self.response.out.write(marca.foto)
        else:
            self.response.out.write('No image')

app = webapp2.WSGIApplication([
    ('/img', Image)
], debug=True)