from fastapi import FastAPI
import uvicorn
import asyncio
from fastapi import APIRouter, Request, Form, Depends
from starlette.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from models.llm import get_completion
from models.stable_diffusion import *
app = FastAPI()
templates = Jinja2Templates(directory='test_templates')


@app.get('/')
def generate_page(request:Request):
    return templates.TemplateResponse(
        'generate_form.html',
        {'request': request})

@app.post('/generate_image/')

async def generate_image(pokemon_1: str, pokemon_2:str | None = None ):
    re = await generate(f"{pokemon_1} with {pokemon_2} pokemon fusion")
    print('hey')


@app.post("/generate_description/")
def generate_description(*, prompt: str = Form(...), request:Request):
    response = get_completion(prompt)
    return templates.TemplateResponse('show_description.html',
                                      {'request':request, 'prompt':prompt, 'response':response})



