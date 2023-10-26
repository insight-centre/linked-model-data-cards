import os
import sys
import yaml
from cerberus import Validator


def load_yaml_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        return None
    except Exception as e:
          print(f"Failed to read the YAML file: {e}")
          sys.exit(1)


def validate_card(card_type, card_name, schema_type):
    cards_dir = 'lmdc/cards'
    schema_dir = 'lmdc/schemas'
    card_path = os.path.join(cards_dir, card_type, "yaml", f"{card_name}.yaml")
    schema_path = os.path.join(schema_dir, f"{schema_type}.yaml")

    card_data = load_yaml_file(card_path)
    if card_data is None:
        print(f"Card '{card_name}' not found.")
        sys.exit(1)

    schema_data = load_yaml_file(schema_path)
    if schema_data is None:
        print(f"Schema '{schema_type}' not found.")
        sys.exit(1)

    v = Validator(schema_data)
    if v.validate(card_data):
        print(f"Card '{card_name}' is valid according to schema '{schema_type}'.")
    else:
        print(f"Card '{card_name}' is not valid according to schema '{schema_type}':")
        for error in v.errors:
            print(f"- {error}: {v.errors[error]}")


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python scripts/validate.py <card_type_dir> <card_name> <schema_type>")
        sys.exit(1)

    card_type = sys.argv[1]
    card_name = sys.argv[2]
    schema_type = sys.argv[3]

    validate_card(card_type, card_name, schema_type)
