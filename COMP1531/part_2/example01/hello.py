    # Import Flask Library
from flask import Flask 
    
'''
all flask  applications must create an application instance, an instance of class Flask 
The web server passes all the requests it receives from clients to this object for handling, using a protoco called Web Server Gateway Interface (WSGI). 
'''    
#create a Flask application instance
app = Flask(__name__)
    
'''
The web browser (i.e. the client application) now sends a request to the web server, which in turn sends the request to the Flask application instance.
The application instance needs to know what code (or function) to run for each invoked URL, so it maintains a mapping of URLs to Python functions. 
This mapping (or association) between a URL and a function is referred to as a route. A route is defined through the app.route function decorator exposed by the application instance, which registers the decorate function as a route as follows:   
'''    
# define a route through the app.route decorator
@app.route("/")
def index():
    return "<h1>Hello World!</h1>"
    
# launch the integrated development web server and run the app on [http://localhost:8085]
if __name__ == "__main__":        
    app.run(debug=True,port=8085)
