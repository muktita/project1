/*Database For Wordle */
-- To enable foreign_keys
PRAGMA foreign_keys = ON;

/* Table for User*/
DROP TABLE IF EXISTS user;
CREATE TABLE user (
    userid integer primary key,
    username varchar,
    pwd varchar,
    UNIQUE(username)
);

/* Table for Game*/
DROP TABLE IF EXISTS game;
CREATE TABLE game (
    gameid integer primary key,
    userid integer,
    correct_word varchar,
    num_guess integer,
    Foreign KEY (userid) REFERENCES (userid)
);

/* Table for Game session*/
DROP TABLE IF EXISTS gameSession;
CREATE TABLE gameSession (
    userid integer,
    gameid integer,
    valid_guess varchar,
    correct_word varchar,
    FOREIGN KEY (userid) REFERENCES (userid),
    FOREIGN KEY (gameid) REFERENCES (gameid),
    FOREIGN KEY (correct_word) REFERENCES (correct_word)
);


