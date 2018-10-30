def main():
    string = filter(str.isalpha, input().lower())
    print(''.join(sorted(set(string))))


if __name__ == '__main__':
    main()