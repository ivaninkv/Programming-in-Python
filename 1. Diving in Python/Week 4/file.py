import os
import tempfile

class File:    

    def __init__(self, full_filepath):
        self.full_filepath = full_filepath
        self.seek = 0

    def __str__(self):
        return self.full_filepath

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.full_filepath) as f:
            f.seek(self.seek)
            result = f.readline()
            self.seek = f.tell()
            if result == '':
                raise StopIteration
            return result

    def __add__(self, second_file):
        new_path = os.path.join(tempfile.gettempdir(), 'new_file.txt')
        with open(new_path, 'w') as f:            
            for line in self:
                f.write(line)
            for line in second_file:
                f.write(line)  
            f.write('\n')
        return File(new_path)


    def write(self, text):
        with open(self.full_filepath, 'w') as f:
            f.write(text)


def main():
    f = File('test.txt')
    print(f.write('a\na\n'))
    f2 = File('test2.txt')
    f2.write('b\nc')
    f3 = f + f2
    f.seek = 1
    f2.seek = 2
    print(f.seek, f2.seek)

    for line in f3:
        print(line, end ='')

if __name__ == '__main__':
    main()