States = {
    "CA": "California",
    "VA": "Virginia",
    "MD": "Maryland",
    "RI": "Rhode Island",
    "NV": "Nevada"
}

print(States["CA"])
print(States["NV"])

nested_dictionary = {
    "CA": {
        "Name": "California",
        "Population": 39557045,
        "Cities": [
            "Fresno",
            "San Francisco",
            "Los Angeles"
        ]
    },
    "VA": {
        "Name": "Virginia",
        "population": 8517685,
        "Cities": [
            "Richmond",
            "Norfolk",
            "Alexandria"
        ]
    },
    "MD": {
        "Name": "Maryland",
        "Population": 6042718,
        "Cities": [
            "Bethesda",
            ""
        ]
    },
    "RI": {
        "Name": "Rhode Island",
        "Population": 1057315,
        "Cities": [
            "Providence",
            "Newport",
            "Warwick"
        ]
    },
    "NV": {
        "Name": "Nevada",
        "Population": 3034392,
        "Cities": [
            "Carson City",
            "Las Vegas",
            "Reno"
        ]
    }
}

print(nested_dictionary["VA"]["Name"])
print(nested_dictionary["MD"]["Cities"][0])
print(nested_dictionary["RI"]["Cities"][2])

print(nested_dictionary.keys())
print(nested_dictionary.items())

print()
for key, value in nested_dictionary.items():
    print(key)
    print(value)
    print("-" * 20)

for state, facts in nested_dictionary.items():
    for attr, value in facts.items():
        print(attr)
        print(value)
        print("-" * 20)
    print("<>" * 20)
worldmap = {
    "R19A":{
        'NAME': "Weibe's room",
        'DESCRIPTION': "You are currently in this class, a parking lot is to the"
                       "north"
        'PATHS'{
                     'NORTH': 'PARKING_LOT'
                 },
    "PARKING_LOT": {
        "NAME": "parking lot",
            'DESCRIPTION': "there are cars here, weibe's class is to the south ",
            'PATHS': {
                "SOUTH": "Weibe's room"
            }
}:

# other variables
current_node = worldmap["Q19A"]
directions = ["NORTH", "SOUTH", "EAST", "WEST", "UP", "DOWN"]
playing = True

# Controller
while playing:
    command = input(">_")
    if command.lower() in ["q", "quit", 'exit']:
        playing = False
    elif command.upper() in directions:
        try:
            room_name = current_node["PATHS"][command.upper()]
            current_node = world_map[room_name]
        except KeyError:
            print("I can't go that way")
    else:
        print("command not recognized")


# other notes

# states
states["AL"] = "Alaska? " # it isn't alaska

# changing dictionary value

states['AL'] = "Alabama" # it's actually Alabama