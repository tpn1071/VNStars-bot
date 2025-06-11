import json
from typing import Dict, Any


def json_file_to_dict(filepath: str) -> Dict[str, Any]:
    """
    Đọc file JSON và trả về dict.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
