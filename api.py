from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

from models.llm import *
from models.stable_diffusion import *
app = FastAPI()
templates = Jinja2Templates(directory='test_templates')


@app.get('/')
async def generate_page(request: Request):
    return templates.TemplateResponse(
        'generate_form.html',
        {'request': request})


@app.post('/generate_image/')
async def generate_image(pokemon_1: str, pokemon_2: str | None = None):
    re = await generate_pokemon(f"{pokemon_1} with {pokemon_2} pokemon fusion")
    print('hey')


@app.post("/generate_description/")
async def generate_description(*, prompt: str = Form(...), request: Request):
    response = generate_pokemon_description(prompt)
    return templates.TemplateResponse('show_description.html',
                                      {'request': request, 'prompt': prompt, 'response': response})