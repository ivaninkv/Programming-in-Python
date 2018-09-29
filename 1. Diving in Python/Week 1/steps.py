import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        num_steps = int(sys.argv[1])
        for step in range(1, num_steps + 1):
            print(' ' * (num_steps - step), end = '')
            print('#' * step)