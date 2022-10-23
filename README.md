# Wordle API for CPSC 499
### Group members: <br/> 
#### Alejandro Ramos Jr (Database & Python code) <br/> Muktita Kim (Database & Python code) <br/> 

### Project </br>
Due to the lack of members, we try to get a as much as we could to make the api calls running </br>
The project is built with flask api with sqlite </br>

### To run the API
#### 1. Install all the dependencies needed
```pip install flask``` <br/>
```sudo apt-get update``` <br/>
```pip install database[aiosqlite]``` <br/>
```sudo apt-get install python3.8 python3-pip``` <br/>
### 2.  Clone the repository 
``git clone https://github.com/muktita/project1.git ``

### 3. Go into the Project1 Directory 
```cd project1```
### 4. Run the program
#### Run the database script to populate the database with correct and valid words
```python3 database.py```
#### Run the API 
```Flask run```

#### Copy this link to run the application
To authenticate the user and password please use <br/>
Username =  username <br/>
Password = password <br/> 
```http://127.0.0.1:5000```<br/>
The check the game use /game <br/>
```http://127.0.0.1:5000/game```


