import json
import time
import uuid
import ast
import random
import re


def generate(data, limit):
    schema = json.loads(data)
    lines = []
    for i in range(limit):
        line = {}
        for key, value in schema.items():
            if value:
                params = value.split(":")
                line[key] = generate_type(params[0], params[1])
        lines.append(line)
    return lines


def generate_type(field_type, args):
    switcher = {
        "str": generate_str,
        "int": generate_int,
        "timestamp": generate_time
    }
    func = switcher.get(field_type)
    return func(args)


def generate_str(args):
    if args == "rand":
        return str(uuid.uuid4())
    elements = ast.literal_eval(args)
    return random.choice(elements)


def generate_int(args):
    matched = re.match(r'rand\((\d+),\s(\d+)\)', args)
    if not matched:
        return "Error string"
    return random.randint(int(matched.group(1)), int(matched.group(2)))


def generate_time(args):
    return time.time()
