import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi import FastAPI,Request,Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.templating import Jinja2Templates
import uvicorn
from dash_app import app as dash_app

app = FastAPI()
# obtenir le chemin directe vers les repertoire models
templates_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
#
static_dir=os.path.abspath(os.path.join(os.path.dirname(__file__), 'static'))
# servir des fichiers statiques
app.mount("/static", StaticFiles(directory=static_dir))

# configurer le model jinja2 pour le rendu du fichier html
templates = Jinja2Templates(directory=templates_dir)

user={'admin':'123'}

# definir la route de la page d'accueil
@app.get("/")
async def home_page(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# definir la route de la page de connexion
@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    if username in user and user[username] == password:
        response = RedirectResponse(url= "/dashboard", status_code=302)
       
        return response
    
    
    return templates.TemplateResponse("login.html", {"request": Request, "error": "Invalid username or password"})