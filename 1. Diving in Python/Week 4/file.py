import os
import tempfile

class File:
    def __init__(self, full_filepath):
        self.full_filepath = full_filepath

    def __str__(self):
        return self.full_filepath

    def __iter__(self):
        return self

    def __next__(self):
        # readlines
        raise StopIteration

    def __add__(self, second_file):
        new_path = os.path.join(tempfile.gettempdir, 'new_file.txt')
        with open(new_path) as f:            
            pass
            #for line in self:
            #    f.write(line)


    def write(self, text):
        with open(self.full_filepath, 'w') as f:
            f.write(text)


def main():
    f = File('test.txt')   
    f.write('tost\n')
    print(f) 

if __name__ == '__main__':
    main()