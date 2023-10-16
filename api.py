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
async def generate_image(request:Request):
    data = await request.json()
    pokemon1 = data.get("first_pokemon")
    pokemon2 = data.get("second_pokemon")

    image = await generate_pokemon(f"{pokemon1} with {pokemon2} pokemon fusion")
    return image

@app.post("/generate_description/")
async def generate_description(*, prompt: str = Form(...)):
    """This gene"""
    response = await generate_pokemon_description(prompt)
    return response