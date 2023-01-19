import json
from os import path

from models.ability_scores.ability_score_bundle import Ability_Score_Bundle

def main():
    name = input("What is your name?")
    filepath = "data/characters/" + name + ".json"

    test = Ability_Score_Bundle()

    if path.exists(filepath):
        print(f'Loading file: {filepath}')
        with open(filepath, 'r') as f:
            json_object = json.load(f)
        test.from_json(json_object)
        print("Load complete!")
            
    else:
        print(f'File does not exist: {filepath}')
        with open(filepath, 'w') as f:
            json_object = json.dumps(test.to_json(), indent=4)
            f.write(json_object)
        print("Saved!")


    test.print_stats()


if __name__ == "__main__":
    main()