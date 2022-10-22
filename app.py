# Import the Flask framework
from flask import Flask, request,make_response,redirect, jsonify
from functools import wraps
import json
import sqlite3

 
# Create an app that hosts the application so that you can use decorators
app = Flask(__name__)

def db_connection():
    con = None
    try:
        con = sqlite3.connect("game.sqlite")
    except sqlite3.error as f:
        print(f)
    return con

@app.route("/game", methods=["GET", "POST"])
def game():
    con = db_connection()
    cursor = con.cursor()

    if request.method == "GET":
        cursor = con.execute("SELECT * FROM game")
        game = [
            dict(user = row[0],id=row[1], incorrect_guess=row[2], correct_guess=row[3], attempts_remain=row[4])
            for row in cursor.fetchall()
        ]
        if game is not None:
            return jsonify(game)

    if request.method == "POST":
        new_user = request.form["user"]
        new_id = request.form["id"]
        new_incorr = request.form["incorrect"]
        new_corr = request.form["correct"]
        new_att = request.form["attempts"]
        
        sql = """INSERT INTO game (user, id,incorrect, correct, attempts)
                 VALUES (?, ?, ?, ?, ?)"""
        cursor = cursor.execute(sql, (new_user, new_id, new_incorr, new_corr,new_att))
        con.commit()
        return f"Game with the id: 0 created successfully", 200  

@app.route("/game/<int:id>", methods=["GET", "PUT", "DELETE"])
def single_game(id):
    con = db_connection()
    cursor = con.cursor()
    game = None
    if request.method == "GET":
        cursor.execute("SELECT * FROM game WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            game = r
        if game is not None:
            return jsonify(game), 200
        else:
            return "Something wrong", 404

    if request.method == "PUT":
        sql = """UPDATE game
                user =?,
                SET id =?,
                    incorrect =?,
                    correct =?
                WHERE id=? """
        user = request.form["user"]
        incorrect = request.form["incorrect"]
        correct = request.form["correct"]
        attempts = request.form["attempts"]
        updated_game = {
            "user": user,
            "id": id,
            "incorrect": incorrect,
            "correct": correct,
            "attempts": attempts,
        }
        con.execute(sql, (user, incorrect, correct, attempts, id))
        con.commit()
        return jsonify(updated_game)


def auth_required(p):
        @wraps(p)
        def decorated(*args, **kwargs):
            auth = request.authorization
            if auth and auth.username == "users" and auth.password == "password":
                 return p(*args, ** kwargs)

            return ('Unauthorized', 401, {'WWW-Authenticate': 'Basic realm="Login Required'})


        return decorated

@app.route("/")
@auth_required
def index():
    if request.authorization and request.authorization.username == "users" and request.authorization.password == "password":
        return "<h1> Authenticated </h1>"
    
    return make_response("Not authenticated", 401, {"WWW-Authenticate" : "Login Required"})

@app.route("/logout")
@auth_required
def logout():
    return redirect(401)




# Start the server
if __name__ == "__main__":
   app.run(debug = True, port=5000)
   # app.run(threaded=True, port=5000)
   
