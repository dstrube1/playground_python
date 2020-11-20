#testCherryPy.py
import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "Hello World!"

cherrypy.quickstart(HelloWorld())
#runs and renders here:
#http://127.0.0.1:8080/

#next:
#https://github.com/cherrypy/cherrypy/tree/master/cherrypy/tutorial
#https://docs.cherrypy.org/en/latest/tutorials.html