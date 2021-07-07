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
