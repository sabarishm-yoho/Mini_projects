from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def home():
    return {
        "Message":"User API created successsfully"
    }

class User(BaseModel):
    User_id:int
    Name:str
    user_dep:str

Users=[
    {
        "User_id":1,
        "Name":"Joe",
        "user_dep":"IT"
    },{
        "User_id":2,
        "Name":"John",
        "user_dep":"IT"
    }
]

@app.get("/user")
def user_info():
    return Users

@app.post("/user")
def add_user(u:User):
    new_id=len(Users)+1
    new_user={
        "User_id":new_id,
        "Name":u.Name,
        "user_dep":u.user_dep    
    }
    Users.append(new_user)
    return {
        "Message":"New user added successfully",
        "User":new_user
    }


@app.put("/user/{User_id}")
def update(id:int,u:User):
    for i in Users:
        if i["User_id"]== id:
            i["Name"]=u.Name
            i["user_dep"]=u.user_dep
            return {
                "Message":"User update successfully",
                "User":i
            }
    return {
        "Message":"User is Not found"
    }

@app.delete("/user/{User_id}")
def delete_user(id:int):
    for j in Users:
        if j["User_id"]==id:
            Users.remove(j)
            return {
                "Message":"User removed successfully",
                "User":j
            }
    return {
        "Message":"User is not found"
    }    

if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)
