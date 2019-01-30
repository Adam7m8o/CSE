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
        "Cities":[
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



'''
Directions = {
    "North":{
        "north" "North" "N" "n",
    },
    "South":{
        "south" "South" "s" "S",
    }<
    "East":{
        "East" "east" "E" "e",
    }<
    "West":{
        "West" "W" "west" "w",
     }
}

'''