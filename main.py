import webapp2
from handlers import MainHandler

app = webapp2.WSGIApplication([
                                  webapp2.Route('/', MainHandler)
], debug=True)