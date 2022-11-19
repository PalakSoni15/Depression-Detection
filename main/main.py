from actions import *

from fastapi import FastAPI, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from fastapi.responses import HTMLResponse
from models import User, Questionaier
from finalyearpbl import input_text
from pprint import pprint
from typing import Optional, Union

import uvicorn

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")

@app.get("/")
def serve_home(request: Request):
    return templates.TemplateResponse("Index.html", {"request": request, "id": id})



@app.get("/login")
def serve_home(request: Request):
    return templates.TemplateResponse("Login.html", {"request": request, "id": id})

@app.get("/blog")
def serve_home(request: Request):
    return templates.TemplateResponse("Blog.html", {"request": request, "id": id})

@app.get("/ex1")
def serve_home(request: Request):
    return templates.TemplateResponse("ex1.html", {"request": request, "id": id})

@app.get("/ex2")
def serve_home(request: Request):
    return templates.TemplateResponse("ex2.html", {"request": request, "id": id})

@app.get("/ex3")
def serve_home(request: Request):
    return templates.TemplateResponse("ex3.html", {"request": request, "id": id})

@app.get("/taketest")
def serve_home(request: Request):
    return templates.TemplateResponse("taketest.html", {"request": request, "id": id})

@app.get("/test2")
def serve_home(request: Request):
    return templates.TemplateResponse("test2.html", {"request": request, "id": id})

@app.get("/result2")
def serve_home(request: Request):
    return templates.TemplateResponse("result2.html", {"request": request, "id": id})

@app.get("/register")
def serve_home(request: Request):
    return templates.TemplateResponse("Registration.html", {"request": request, "id": id})

@app.get("/asses")
def serve_home(request: Request):
    return templates.TemplateResponse("assesment.html", {"request": request, "id": id})

@app.get("/result1")
def serve_home(request: Request):
    return templates.TemplateResponse("result1.html", {"request": request, "id": id})


@app.post("/depression")
def serve_home(text: str):
    depression = input_text(text)
    return templates.TemplateResponse("result2.html", {"request": {}, "id": id, "response": {"depression": depression}})


@app.post("/result")
def serve_home( que1: Optional[str] = Form(), 
                que2: Optional[str] = Form(), 
                que3: Optional[str] = Form(), 
                que4: Optional[str] = Form(), 
                que5: Optional[str] = Form(), 
                que6: Optional[str] = Form(), 
                que7: Optional[str] = Form(), 
                que8: Optional[str] = Form(), 
                que9: Optional[str] = Form(), 
                que10: Optional[str] = Form(), 
                que11: Optional[str] = Form(), 
                que12: Optional[str] = Form(), 
                que13: Optional[str] = Form(),
                que14: Optional[str] = Form(), 
                que15: Optional[str] = Form(), 
                que16: Optional[str] = Form(), 
                que17: Optional[str] = Form(), 
                que18: Optional[str] = Form(), 
                que19: Optional[str] = Form(), 
                que20: Optional[str] = Form(), 
                que21: Optional[str] = Form(), 
                que22: Optional[str] = Form(), 
                que23: Optional[str] = Form(), 
                que24: Optional[str] = Form(), 
                que25: Optional[str] = Form(), 
                que26: Optional[str] = Form(), 
            ):                

    requests = [que1, que2, que3, que4, que5, que6, que7, que8, que9, que10, que11, que12, que13, 
                que14, que15, que16, que17, que18, que19, que20, que21, que22, que23, que24, que25, que26]

    print(requests)

    response = assess_results(requests)
    return templates.TemplateResponse("result1.html", {"request": {}, "id": id, "response": response})
    # return {"message": "Some message"}


@app.post("/validate_registeration/")
def register(item:User):
    if registerUser(item):
        return {"Message": "User Registered successfully", "success": True}
    return {"Message": "Unable to register user", "success": False}

@app.post("/validate_login/")
def login(item:User):
    uname = item['uname']
    password = item['password']

    if validate(uname, password):
        return {"Message": "Login Succesfull", "success": True}
    return {"Message": "Invalid Login/Password", "success": False}


if __name__ == "__main__":
    uvicorn.run(app)