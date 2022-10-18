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


words = ['programming', 'tiger', 'lamp', 'television',
'laptop', 'water', 'microscope', 'doctor', 'youtube',
'projects']

random_word = random.choice(words)

print('our random word', random_word)

print('*********** WORD GUESSING GAME ***********')

user_guesses = ''
chances = 10

while chances > 0:
    wrong_guesses = 0
    for character in random_word:
        if character in user_guesses:
            print(f"Correct guess: {character}")
        else:
            wrong_guesses += 1
            print('_')

    if wrong_guesses == 0:
        print("Correct.")
        print(f"Word : {random_word}")
        break
    guess = input('Make a guess: ')
    user_guesses += guess

    if guess not in random_word:
        chances -= 1
        print(f"Wrong. You have {chances} more chances")

        if chances == 0:
            print('game over')


# Start the server
if __name__ == "__main__":
   app.run(debug = True, port=5000)
   # app.run(threaded=True, port=5000)
   
