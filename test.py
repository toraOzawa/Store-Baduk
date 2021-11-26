from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uuid

app = FastAPI()

permissionKey = ""
class Game(BaseModel):
    sgf: str

# ToDo create additional models and refactor code so that databases makes a bit more sense 

databases = {
    "database_id": {
        "name": "placeholder name",
        "moveTables": [[]] # array of move lists
                           # each list contains a dicitionary with the count and associated move 
    }
}

@app.get("/")
def home():
    return {"Data" :  "Testing"}

@app.get("/about")
def about():
    return {"Data": "About"}

@app.post("/create-database/{secret}/{database_name}")
def create_database(secret: str, database_name: str):
    if secret == permissionKey:
        id = uuid.uuid1()
        databases[str(id)] = {"name": database_name, "moveTables": [[]]} # should be a model 
        return str(id)
    else:
        return {"Error": "permission to create database not granted"} # change to actual error 

@app.post("/add-game/{database_id}")
def add_game(database_id: str, game: Game):
    result = ''
    if not database_id in databases: 
        return {"Error": "database not found"} # change to actual error 

    move_list = list(game.sgf.split("-"))

    move_index = 0
    for move in move_list:
        unique = False
        if (len(databases[database_id]["moveTables"]) == move_index):
            databases[database_id]["moveTables"].append([]) # is this the correct way to append an empty array?

    
        moves = databases[database_id]["moveTables"][move_index]
        if move in moves:
            moves[move]["count"] = moves[move]["count"] + 1
            result = result + str(moves.index(move))
        else:
            moves[move] = { "count": 0 }
            result = result + str(moves.index(move))
            break
        move_index += 1

    return {"game-key": result}





