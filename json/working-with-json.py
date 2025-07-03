import json

sample = {
    "cat1" : {
        "a1": 1,
        "b1": 1,
    },
    "cat2" : {
        "a2": 2,
        "b2": 2,
        "c2": 2,
    },
    "cat3" : {
        "a3": 3,
        "b3": 3,
        "c3": 3,
        "d3": 3,
    },
}

with open("sample.json", mode="w", encoding="utf-8") as write_file:
    json.dump(sample, write_file)