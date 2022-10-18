from flask import Flask, redirect
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
 
app = Flask(__name__)
auth = HTTPBasicAuth()
 
 
users = {
   "Alejandro": generate_password_hash("Niners"),
   "George": generate_password_hash("bye")
}
 
@auth.verify_password
def verify_password(username, password):
   if username in users and \
           check_password_hash(users.get(username), password):
       return username
 
@app.route('/')
@auth.login_required
def index():
   return "Hello, {}!".format(auth.current_user())
# Start the server
if __name__ == "__main__":
  app.run(debug = True, port=5000)
  # app.run(threaded=True, port=5000)