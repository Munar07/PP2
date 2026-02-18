import json

source = json.loads(input())
patch = json.loads(input())

def apply_patch(src, p):
    for key, value in p.items():
        if value is None:
            if key in src:
                del src[key]
        elif isinstance(value, dict) and isinstance(src.get(key), dict):
            apply_patch(src[key], value)
        else:
            src[key] = value

apply_patch(source, patch)
print(json.dumps(source, sort_keys=True, separators=(',', ':')))
