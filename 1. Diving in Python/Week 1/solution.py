import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        digit_string = sys.argv[1]
        sum = 0
        for digit in digit_string:
            sum += int(digit)

        print(sum)