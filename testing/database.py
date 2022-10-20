import sqlite3
import json
from unittest import result 
conn = sqlite3.connect('wordle.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS user (user_id INTERGER PRIMARY KEY AUTOINCREMENT, username VARCHAR, passwd VARCHAR)""")

c.execute("""CREATE TABLE IF NOT EXISTS game (game_id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, num_guess INTEGER, FOREIGN KEY (user_id) REFERENCES user(user_id))""")

c.execute("""CREATE TABLE IF NOT EXISTS game_session (game_id INTEGER PRIMARY KEY, user_id INTEGER, valid_guess VARCHAR, correct_word VARCHAR, FOREIGN KEY (game_id) REFERENCES game(game_id))""")
c.execute("""CREATE TABLE IF NOT EXISTS valid_words (valid_words VARCHAR)""")
c.execute("""CREATE TABLE IF NOT EXISTS correct_word (correct_words VARCHAR)""")

f = open('valid.json')
valid = json.loads(f)

for words in valid:
    c.execute("INSERT INTO valid_words (valid_words) VALUES(?)", (words,))
f.close()

g = open('correct.json')
correct = json.loads(g)

for word in correct:
    c.execute("INSERT INTO correct_word (correct_words) VALUES(?)", (word, ))
g.close()

c.execute("SELECT *FROM correct_word")
result = c.fetchall()
print(result)
conn.commit
