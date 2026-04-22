import json
from pathlib import Path


def read_json(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)
    

def write_json(path: Path, data):
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
