## Muktita Kim

import json
from opcode import opname
import sqlite3

conn = sqlite3.connect('wordle.db') # Create a database to store the db
c = conn.cursor()

# Open and load the json file
f = open('correct.json')
data = json.loads(f)

# Populate the correct_words
for val in data:
    c.execute("INSERT INTO game (correct_word) VALUES (?)", val)
f.close()

g = open('valid.json')
validData = json.load(g)

for val in validData:
    c.execute("INSERT INTO game (valid_guess) VALUES (?)", val)
g.close()
conn.commit
