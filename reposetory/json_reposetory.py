import json
def read_jason(path):
    try:
        with open(path, "r", encoding='utf-8') as file:
            return json.load(file)
    except Exception:
        return []
