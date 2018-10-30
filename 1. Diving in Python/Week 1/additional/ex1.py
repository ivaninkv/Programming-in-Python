import re


def main():
    string1, string2 = input().lower(), input().lower()
    string2 = set(''.join(re.findall('[a-z]', string2)))
    used_symbols = set()
    for symbol2 in string2:
        if symbol2 not in used_symbols:
            print(symbol2, end=' ')
            used_symbols.add(symbol2)
            founded = False
            for i in range(len(string1)):
                if string1[i] == symbol2:
                    founded = True
                    print(i+1, end=' ')
            if not founded:
                print(None, end=' ')
            print()    

if __name__ == '__main__':
    main()