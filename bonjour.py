#!/usr/bin/python3


def bonjour(name):
    print('Hello %s!' % name)


if __name__ == '__main__':
    import sys
    bonjour('world', sys.argv[1])
