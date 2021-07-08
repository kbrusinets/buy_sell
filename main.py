from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from models import templates

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("dashboard.html", {
        "request": request
    })

@app.get("/1")
async def root(request: Request):
    return templates.TemplateResponse("profile_card.html", {
        "request": request
    })

@app.get("/1/edit")
async def root(request: Request):
    return templates.TemplateResponse("profile_edit.html", {
        "request": request
    })
