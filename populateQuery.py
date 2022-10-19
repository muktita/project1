import json
import sqlite3

conn = sqlite3.connect('wordle.db') # Create a database to store the db
c = conn.cursor()

# Open and load the json file
f = open('correct.json')
data = json.load(f)

# Populate the correct_words
for val in data:
    c.execute("INSERT INTO game (correct_word) VALUES ()", val)

conn.commit
c.close()
