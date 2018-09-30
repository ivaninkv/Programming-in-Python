import tempfile
import argparse
import json
import os

def GetData(file_path, key):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:
            data = f.read().strip()
            if data != '':
                d = json.loads(data)
                print(*d.get(key), sep=', ')
    else:
        print(None)

def WriteData(file_path, key, value):
    d = {}

    if os.path.isfile(file_path):
        with open(file_path, 'r') as f:  
            data = f.read().strip()
            if data != '':      
                d = json.loads(data)        

    with open(file_path, 'w') as f:
        cur_value = d.get(key) or []        
        if value[0] not in cur_value:
            cur_value += value
        d[key] = cur_value
        f.write(json.dumps(d, sort_keys=True, indent=4))
        f.write('\n')        

if __name__ == '__main__':
    # https://docs.python.org/3/howto/argparse.html
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key', help='Ключ словаря по которому нужно вернуть или записать значение.')
    parser.add_argument('-v', '--value', help='Значение для записи в файл для конкретного ключа.', nargs='+')
    args = parser.parse_args()
    
    storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')    
    # storage_path = 'storage.data'
    if args.value is None:
        GetData(storage_path, args.key)
    else:
        WriteData(storage_path, args.key, args.value)