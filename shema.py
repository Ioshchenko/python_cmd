import json
import time
import uuid
import ast
import random
import re

from console_exception import ConsoleException


def generate(data, limit):
    schema = json.loads(data)
    lines = []
    for i in range(limit):
        line = {}
        for key, value in schema.items():
            if value:
                params = value.split(":")
                line[key] = _generate_type(params[0], params[1])
        lines.append(line)
    return lines


def _generate_type(field_type, args):
    switcher = {
        "str": _generate_str,
        "int": _generate_int,
        "timestamp": _generate_time
    }
    func = switcher.get(field_type)
    if not func:
        raise ConsoleException("Type: {} not supported.".format(field_type))
    return func(args)


def _generate_str(args):
    if args == "rand":
        return str(uuid.uuid4())
    elements = ast.literal_eval(args)
    return random.choice(elements)


def _generate_int(args):
    matched = re.match(r'rand\((\d+),\s(\d+)\)', args)
    if not matched:
        raise ConsoleException("Wrong format: {}. Example: rand(n1, n2)".format(args))
    return random.randint(int(matched.group(1)), int(matched.group(2)))


def _generate_time(args):
    return time.time()
