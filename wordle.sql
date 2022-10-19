/*Database For Wordle */

/* Table for User*/
DROP TABLE IF EXISTS user;
CREATE TABLE user (
    id int primary key,
    username varchar,
    pwd varchar,
);

/* Table for Game*/
DROP TABLE IF EXISTS game;
CREATE TABLE game (
    id itn primary key,
    user_id int references user(id),
    correct_word varchar,
    win boolean,
    guess int
);

