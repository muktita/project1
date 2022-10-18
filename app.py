# Import the Flask framework
from flask import Flask, request,make_response,redirect
from functools import wraps

 
# Create an app that hosts the application so that you can use decorators
app = Flask(__name__)

def auth_required(p):
        @wraps(p)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if auth and auth.username == "username" and auth.password == "password":
                 return p(*args, ** kwargs)

            return ('Unauthorized', 401, {'WWW-Authenticate': 'Basic realm="Login Required'})


        return decorated

@app.route("/")
@auth_required
def index():
    if request.authorization and request.authorization.username == "username" and request.authorization.password == "password":
        return "<h1> Authenticated </h1>"
    
    return make_response("Not authenticated", 401, {"WWW-Authenticate" : "Login Required"})

@app.route("/logout")
def logout():
    return redirect(401)

@app.route("/page")
@auth_required
def ok():
    return "ehllo"


# Start the server
if __name__ == "__main__":
   app.run(debug = True, port=5000)
   # app.run(threaded=True, port=5000)
   
