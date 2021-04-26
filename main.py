from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from module.scraper import Scraper
from pydantic import BaseModel

class scraper_req(BaseModel):
    url: str
    keywords: str

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    syntax = {}
    syntax["request"] = request
    return templates.TemplateResponse("index.html",  syntax)
 
@app.post("/scraper/")
async def extract_data(scraperReq: scraper_req):
    url = scraperReq.url
    extracted_text = Scraper(url)
    return {"data":extracted_text}
