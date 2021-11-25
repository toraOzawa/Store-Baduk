from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Game(BaseModel):
    sgf: str


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

@app.post("/add-game/{database_id}")
def add_game(database_id: str, game: Game):
    result = ''
    if not database_id in databases: 
        return {"Error": "database not found"}

    move_list = list(game.split("-"))

    count = 0
    for move in move_list:
        unique = False
        if (len(databases[database_id]["moveTables"]) == count):
            databases[database_id]["moveTables"].append([]) # is this the correct way to append an empty array?

    
        moves = databases[database_id]["moveTables"][count]
        if move in moves:
            moves[move]["count"] = moves[move]["count"] + 1
            result = result + str(moves.index(move))
        else:
            moves[move] = { "count": 0}
            result = result + str(moves.index(move))
            break

    return {"game-key": result}





