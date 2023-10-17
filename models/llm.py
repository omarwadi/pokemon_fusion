import openai
import langchain
from langchain import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import ResponseSchema
from langchain.output_parsers import StructuredOutputParser
from langchain.chat_models import AzureChatOpenAI
from typing import Optional, Literal
from models.stable_diffusion import generate_pokemon

# openai.api_key = "18f15fe7944c47fdaf38614a94403a90"
# openai.api_base = "https://pokemongpt.openai.azure.com/"
# openai.api_type = "azure"
# openai.api_version = "2023-05-15"

GPT_4 = "gpt-4"
GPT_4_32K = "gpt-4-32k"
MODEL_NAMES = Literal["gpt-4", "gpt-4-32k"]


LLM_MODEL_PARAMS = {
    GPT_4: {
        "deployment_name": "test",
        "model_name": GPT_4,
    },
}

AZ_LLM_PARAMS = {
    "openai_api_type": "azure",
    "openai_api_version": "2023-05-15",
    "temperature": 0,
    "openai_api_base": "https://pokemonGPT.openai.azure.com/",
    "openai_api_key": "5d482a5723e742b69da51b233bee4240",
}


similar_pokemons = "Entei pokemon and Kyurem pokemon" #Its hardcodded for now, will be changed later
deployment_name = "test"

DESCRIPTION_TEMPLATE = """

    ###Rules:
    - For uncertainty, use "None".
    - Avoid Mistakes.

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

    Based on user's input, generate.

    user input:
    prompt, similar_pokemons
    """



def get_llm(model_name: MODEL_NAMES):

def get_prompt():
    '''
        This function takes nothing and it adds the response schema with the description template 
        so the model outputs the response in a way similir to what we want 
    '''
    name_schema = ResponseSchema(
        name="name", description="Whats the name of the pokemon?"
    )

    origin_schema = ResponseSchema(
        name="name_origin", description="Where the name came from? Origin of the name?"
    )
    category_schema = ResponseSchema(
        name="category",
        description="Whats the pokemon category?\
                                    like charmander it's known as the lizard pokemon or\
                                    bulbasaur known as the seed pokemon",
    )
    hp_schema = ResponseSchema(name="HP", description="Whats the pokemon's HP?")
    atk_schema = ResponseSchema(
        name="attack", description="Whats the pokemon's attack?"
    )
    def_schema = ResponseSchema(
        name="defence", description="Whats the pokemon's Defence?"
    )
    sp_atk_schema = ResponseSchema(
        name="special_attack", description="Whats the pokemon's Special attack?"
    )
    sp_def_schema = ResponseSchema(
        name="special_defence", description="Whats the pokemon's Special Defence?"
    )
    spd_schema = ResponseSchema(name="Speed", description="Whats the pokemon's Speed?")
    totalstats_schema = ResponseSchema(
        name="total_stats", description="Whats the sum of all the previous stats?"
    )
    height_schema = ResponseSchema(
        name="height",
        description="Whats the pokemon's height? based on the 2 pokemons given",
    )
    weight_schema = ResponseSchema(
        name="weight",
        description="Whats the pokemon's Weight? based on the 2 pokemons given",
    )
    gender_schema = ResponseSchema(
        name="gender",
        description="Whats the pokemon's Gender?\
                                    give a percentage, and if its a legendary it should be unknown, unless the user decides ",
    )
    levelingrate_schema = ResponseSchema(
        name="leveling_rate",
        description="Whats the pokemon's Leveling rate?\
                                    based on the 2 pokemons given",
    )
    catchrate_schema = ResponseSchema(
        name="catch_rate",
        description="Whats the pokemon's Catch rate?\
                                    based if its a legendary or not give it a value",
    )
    location_schema = ResponseSchema(
        name="location",
        description="Whats the pokemon's Location? where could it be found?",
    )
    basefriendship_schema = ResponseSchema(
        name="base_friendship",
        description="Whats the pokemon's Base friendship?based on the 2 pokemons given",
    )
    egggroup_schema = ResponseSchema(
        name="egg_group",
        description="Whats the pokemon's Egg group?based on the 2 pokemons given",
    )
    abilities_schema = ResponseSchema(
        name="abilities",
        description="What are the pokemon's Abilities? what each ability do exactly? based on the 2 pokemons given",
    )
    hiddenabilities_schema = ResponseSchema(
        name="hidden_ability",
        description="Whats the pokemon's Hidden Ability?what does the ability do exactly?",
    )
    weakto_schema = ResponseSchema(
        name="weak_to", description="Whats the pokemon's Weak to?"
    )
    immuneto_schema = ResponseSchema(
        name="immune_to",
        description="Whats the pokemon's Immune to? based on the type or types the user gave you",
    )
    resistantto_schema = ResponseSchema(
        name="resistant_to",
        description="Whats the pokemon's Resistant to? based on the type or types the user gave you",
    )
    basemovesset_schema = ResponseSchema(
        name="base_moves",
        description="What are the pokemon's Base Moves? generate them and output\
                                        them as key:value and in our case its move:move name",
    )
    # movesset_schema = ResponseSchema(
    #     name="moves_set",
    #     description="What are the pokemon's Base Moves? generate them and output\
    #                                     them as key:value and in our case its Level that the pokemon needs to reach:move name\
    #                                     give it moves up to level 80",
    # )
    specialmoves_schema = ResponseSchema(
        name="special_move",
        description="What's the pokemon's Special Move? ***THIS IS ONLY FOR LEGENDARY POKEMONS***\
                                        if the pokemon was legendary give it a special move that suits\
                                        its type that identifies it and make it stand out compared to other pokemons,\
                                        and when does it learn the move, also give values for the following:\
                                        Description: describe what the move do\
                                        PP:	How many times it could be used before running out of uses\
                                        Power: its power, it could exceeds 100\
                                        Accuracy: the chance for it to hit, in percentage\
                                        and output them in a json format",
    )
    resistantto_schema = ResponseSchema(
        name="resistant_to",
        description="Whats the pokemon's Resistant to? based on the type or types the user gave you",
    )
    description_schema = ResponseSchema(
        name="description",
        description="Whats the pokemon's description? an introduction about the pokemon and what can\
                                        it do with some trivia and fun fact, where it's best used\
                                        and when, main role in the team, other Pokemons that work\
                                        very well with it and complete each others.",
    )

    response_schemas = [
        resistantto_schema,
        specialmoves_schema,
        # movesset_schema,
        basemovesset_schema,
        resistantto_schema,
        immuneto_schema,
        weakto_schema,
        hiddenabilities_schema,
        abilities_schema,
        egggroup_schema,
        basefriendship_schema,
        location_schema,
        catchrate_schema,
        levelingrate_schema,
        gender_schema,
        weight_schema,
        height_schema,
        name_schema,
        origin_schema,
        category_schema,
        hp_schema,
        atk_schema,
        def_schema,
        sp_atk_schema,
        sp_def_schema,
        spd_schema,
        totalstats_schema,
        description_schema,
    ]

    output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
    format_instructions = output_parser.get_format_instructions()
    prompt_template = ChatPromptTemplate.from_template(
        template=f"{DESCRIPTION_TEMPLATE}."
        + "\n{format_instructions}\n{similar_pokemons}\n{prompt}",
        partial_variables={
            "format_instructions": format_instructions,
        },
    )

    return prompt_template, output_parser

    """
        returns model's information 
    """
    streaming = False
    model_selection = [GPT_4, GPT_4_32K]
    if model_name in model_selection:
        return AzureChatOpenAI(
            **AZ_LLM_PARAMS,
            **LLM_MODEL_PARAMS[model_name],
            streaming=streaming,
        )

def completion(model_name: MODEL_NAMES, prompt: ChatPromptTemplate, input_dict: dict,):
    """
        Return the model's response
    """
    chain = LLMChain(
        llm=get_llm(model_name),
        prompt=prompt,
    )
    response = chain(
        input_dict,
    )

    return response

async def generate_pokemon_description(prompt: str):
    """
        calls the completion function to get the model's response.
        After that it formats the response so the output becomes a json and returns it. 
    """
    prompt_template, output_parser = get_prompt()
    response = completion(
        model_name=GPT_4,
        prompt=prompt_template,
        input_dict={"prompt": prompt, "similar_pokemons": similar_pokemons},
    )
    try:
        response_text_json = output_parser.parse(response["text"])
    except Exception as e:
        raise e

    if response_text_json:
        return response_text_json
    else:
        return None
