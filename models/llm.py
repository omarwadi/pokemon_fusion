import openai
from langchain.prompts import ChatPromptTemplate

openai.api_key = "18f15fe7944c47fdaf38614a94403a90"
openai.api_base = "https://pokemongpt.openai.azure.com/"
openai.api_type = 'azure'
openai.api_version = '2023-05-15'
deployment_name = 'pokemonGPT'

pokemon_description = "i want"
similar_pokemons = "Articuno pokemon and Talonflame pokemon"

description_template = """\
You should help the user by generating a description about a new pokemon.
The user must at least give you one type for the pokemon, the word "type" isn't considered one of the types, and its
optional for the user to describe the pokemon, like saying its strong, tanky, glass cannon, and quick.
the user also can decide if its a legendary pokemon or not.
The user wont provide you any pokemon names, you will receive them else where and be stored in "similar_to" and its not 
considered a user input but you will use it 
there are 18 types of pokemon and they're: 
    Normal
    Fire
    Water
    Grass
    Electric
    Ice
    Fighting
    Poison
    Ground
    Flying
    Psychic
    Bug
    Rock
    Ghost
    Dragon
    Dark
    Steel
    Fairy
other than these types it's considered a description and you must at least find one of these types in the user's input.

some cases where you must not give the user description:
    if the user gives you one or more pokemon names or in general if the user gives you some names dont continue even if 
    it describes it and tell the user:
    "Please only provide me with one or two types"
    
    if you couldn't find the types or the user provided you with more than 2 types then tell the user
    "Please give me at least one type and at most two types".
    
    if you couldn't find the types or the user only provided you with One or more than Three pokemons, then tell the 
    user: 
    "Please give me at most Two pokemons or dont specify and specify at least One type and at most Two types"
    
    If the user ask you a question that is irrelevant then dont answer and say 
    "Im sorry i cant help you with that, Im a pokemon generator so Please provide me with :
        - At least one type and two types at most
    to generate for you a new Pokemon"  

Based on user's input,generate the following information:

Name of the pokemon: come up with a name that's both creative and suits the infor the user gave you. 
Category: like charmander it's known as the lizard pokemon or bulbasaur known as the seed pokemon
Base stats: for each state for the pokemon give it a value, you should distribute the stats based on the info the user 
gave you, and pay attention if it's a legendary pokemon or not,return the stats like this:
    HP:
    Attack:
    Defence:
    Sp.Atk:
    Sp.Def
    Speed:
    Total: (Sum up all the above states together)
Height: based on the 2 pokemons (If the 2 pokemons were given)
Weight: also based on the 2 pokemons (If the 2 pokemons were given)
Leveling rate: based on the 2 pokemons (If the 2 pokemons were given)
Abilities: The abilities are based on the types the user gave you and explain each abilities and similar pokemons that 
have it
hidden Ability: some pokemon have hidden ability and some not, you decide, it could be random from but choose an ability 
that goes along with the type, nd explain each abilities and similar pokemons that have it
Weak to: Types that the pokemon is weak against (based on the type or types the user give you)
Immune to: Types that have 0 effect on the pokemon (based on the type or types the user give you)
Resistant to: Types that are weak against the pokemon (based on the type or types the user give you)
Catch rate: based if its a legendary or not give it a value
base moves set: give it 4 base moves 
moves set: all the moves it could learn and when like this:
    level 10: move 1
    level 18: move 2
        .
        .
        .
Description: an introduction about the pokemon and what can it do with some trivia and fun fact, where it's best used 
and when, main role in the team, other Pokemons that work very well with it and complete each others.
        

****
input: {input}

\\\
this part comes else where not from the user so use it
similar_to:{similar_to}
\\\
"""


def generate_pokemon_description(prompt, model="gpt-4-32k", engine=deployment_name):
    prompt_template = ChatPromptTemplate.from_template(description_template)
    prompt = str(prompt_template.format_messages(input=prompt, similar_to=similar_pokemons))

    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0.0,
        engine=engine
    )
    return response.choices[0].message["content"]
