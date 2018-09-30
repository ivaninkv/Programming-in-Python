import json
import functools

def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = json.dumps(func(*args, **kwargs))
        return result
    return wrapped

@to_json
def get_data():
    return {'data': 42}

@to_json
def get_list():
    return [1, 2, 4]    

if __name__ == '__main__':
    print(get_data())  # вернёт '{"data": 42}'
    print(get_data == str({'data': 42}))
    print(get_list())

    with open('test.txt', 'w') as f:
        f.write(get_data())

    with open('test.txt', 'r') as f:
        d = json.load(f)
        print(d)