import json
from typing import Any


class FileStorage:
    @staticmethod
    def save_to_json(filename: str, data: Any):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
