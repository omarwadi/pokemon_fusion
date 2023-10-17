################   JUST FOR TESTING   ################

import asyncio
from models.llm import generate_pokemon_description
from models.stable_diffusion import generate_pokemon


async def create_pokemon():
    des = " i want it to all-rounder pokemon and it to be a Dark with Ghost type"
    desc = await generate_pokemon_description(des)
    return desc


async def main():
    desc = await create_pokemon()
    print(desc)

asyncio.run(main())

