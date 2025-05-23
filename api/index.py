import json

def handler(request, response):
    from urllib.parse import parse_qs
    from os.path import join, dirname

    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Content-Type"] = "application/json"

    query = parse_qs(request.query_string.decode())
    names = query.get("name", [])

    try:
        with open(join(dirname(__file__), '../students.json')) as f:
            data = json.load(f)
        
        marks = [data.get(name, None) for name in names]
        return response.json({"marks": marks})
    
    except Exception as e:
        return response.json({"error": str(e)}, status=500)
