import json
from typing import Dict, Any


def dict_to_json_file(data: Dict[str, Any], filepath: str) -> None:
    """
    Chuyển dict thành JSON và ghi đè lên file.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
