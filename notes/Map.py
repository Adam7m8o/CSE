worldmap = {
    "OMD":{
        'NAME': "outskirts middle down",
        'DESCRIPTION': "You Awoke here to east and west there is more forest"
        'PATHS'{
            'EAST': 'OLD',
            'WEST': 'ORD',
                 },
    "OLD": {
        "NAME": "Outskirts left down",
            'DESCRIPTION': "You are surrounded by shrubbery, there is more forest to the North and West",
            'PATHS': {
                "WEST": "OMD",
                "NORTH": "OLM",
            },
    "ORD":{
        "NAME": "Outskirts right down",
        "DESCRIPTION": "Your'e surrounded by shrubbery, there's glint from one of the bushes"
                       "There is more forest to the North and to the West",
        "PATHS":{
            "NORTH": "ORM",
            "WEST": "OMD",
        },
    },
    "OLM"{
        "NAME": "Outskirts left middle",
        "DESCRIPTION": "You're surrounded by shrubbery, there are paths to the North and the south",
        "PATHS": {
            "NORTH": "OLU",
            "South": "OLD",
        },
    },
},
