class FileReader:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        try:
            with open(self.file_name) as f:
                return f.read()
        except IOError:
            return ''
            

def main():
    reader = FileReader('methodi_part_2.slides.html')
    print(reader.read())

if __name__ == '__main__':
    main()   