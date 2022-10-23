from flask import Flask, request,make_response,redirect, jsonify
from functools import wraps
import json
import sqlite3

 
# Create an app that hosts the application so that you can use decorators
app = Flask(__name__)

def db_connection():
    con = None
    try:
        con = sqlite3.connect("user.sqlite")
    except sqlite3.error as f:
        print(f)
    return con

@app.route("/user", methods=["GET", "POST"])
def user():
    con = db_connection()
    cursor = con.cursor()

    if request.method == "GET":
        cursor = con.execute("SELECT * FROM user")
        user = [
            dict(id = row[0],username=row[1], password=row[2])
            for row in cursor.fetchall()
        ]
        if user is not None:
            return jsonify(user)

    if request.method == "POST":
        new_id = request.form["id"]
        new_user = request.form["user"]
        new_password = request.form["password"]
       
        
        sql = """INSERT INTO user(user, id,passowrd)
                 VALUES (?, ?, ?)"""
        cursor = cursor.execute(sql, (new_user, new_id, new_password))
        con.commit()
        return f"User with the id: 0 created successfully", 200

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
def db_connection():
    con = None
    try:
        con = sqlite3.connect("game_session.sqlite")
    except sqlite3.error as f:
        print(f)
    return con

@app.route("/word", methods=["GET", "POST"])
def game_session():
    con = db_connection()
    cursor = con.cursor()

    if request.method == "GET":
        cursor = con.execute("SELECT * FROM word")
        game_session = [
            dict(five_letter = row[0],corret_word=row[1])
            for row in cursor.fetchall()
        ]
        if game_session is not None:
            return jsonify(game_session)

    if request.method == "POST":
        new_word = request.form["user"]
        new_correct = request.form["id"]
   
        
        sql = """INSERT INTO game (user, id)
                 VALUES (?, ?)"""
        cursor = cursor.execute(sql, (new_word, new_correct))
        con.commit()
        return f"game_session with the id: 0 created successfully", 200    

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

@app.route("/start")
@auth_required
def start():
    con = sqlite3.connect('game_session.sqlite')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM game_session ")
    row = cursor.fetchall()

@app.route("/five_words")
@auth_required
def five():
    con = sqlite3.connect('game_session.sqlite')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM game_session ")
    row = cursor.fetchall()

@app.route("/game_in_progress")
@auth_required
def game_id():
    con = sqlite3.connect('game.sqlite')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM game ")
    row = cursor.fetchall()





# Start the server
if __name__ == "__main__":
   app.run(debug = True, port=5000)
   # app.run(threaded=True, port=5000)
   
   
