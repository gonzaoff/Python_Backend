from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()




# Tercer intento de base de datos. 
# Definiendo el tipo de cada variable en una clase. Campturando ID's
class User(BaseModel):
    id: int
    name: str
    surname : str
    age: int
    url: str

users_list = [User(id=1, name="Gonzalo", surname="Escobar", age=22, url="/sibofit"),
        User(id=2, name="Federico", surname="Escobar", age=36, url="/fyge"),
        User(id=3, name="Natalia", surname="Escobar", age=28, url="/natiesc")]

# Usando Path.
@app.get("/user/{id}")
async def user(id:int):
    return search_user(id)

""""
@app.get("/user/{id}/{name}")
async def user(id:int,name:str):
    return search_user(id)
"""

# Usando Query.
@app.get("/userquery/")
async def user(id:int):
    return search_user(id)

urlquery = "http://127.0.0.1:8000/userquery?id=1"

"""
@app.get("/userquery/")
async def user(id:int,name:str):
    return search_user(id)

urlquery = http://127.0.0.1:8000/userquery?id=1&name=Gonzalo
"""

# Funcion resumen
def search_user(id:int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error":"No se ha encontrado el usuario"}
    

"""
uvicorn users:app --reload
"""