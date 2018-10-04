import functools
import json


def to_json(func):

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)

    return wrapped