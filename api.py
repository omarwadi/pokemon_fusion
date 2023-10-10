from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from models.llm import *
from models.stable_diffusion import *
app = FastAPI()
templates = Jinja2Templates(directory='test_templates')

origins = [
    "http://localhost:3000",  # Update with the correct URL of your Next.js app
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/')
async def generate_page():
    return print('Hello')


@app.post('/generate_image/')
async def generate_image(pokemon_1: str, pokemon_2: str | None = None):
    re = await generate_pokemon(f"{pokemon_1} with {pokemon_2} pokemon fusion")
    print('hey')


@app.post("/generate_description/")
async def generate_description(*, prompt: str = Form(...), request: Request):
    """This gene"""
    response = await generate_pokemon_description(prompt)
    return response