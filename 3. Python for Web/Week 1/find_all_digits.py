import re


def find_all_digits(text):
    exp = r'\d+'  # Тут напишите своё регулярное выражение  
    return re.findall(exp, text)


# def main():
#     print(find_all_digits('a123b45с6d'))

# if __name__ == '__main__':
#     main()