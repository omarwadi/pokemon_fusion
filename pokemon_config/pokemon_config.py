import json


def get_config_file():
    config = open('/Users/oalwadi001/PycharmProjects/pokemon_fusion/pokemon_config/pokemon_config.json', 'r')
    config = json.load(config)[0]
    return config
