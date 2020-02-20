#!/usr/bin/env python3

from collections import namedtuple
from os import listdir

Library = namedtuple("Library", ['n_books', 'signup_time', 'throughput', 'books'])

Input = namedtuple("Input", ['n_books', 'n_libraries', 'n_days', 'books', 'libraries'])


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip(*args)


def read_input(fname):
    with open(fname) as f:
        n, t, m = f.readline().split()
        books = f.readline().split()
        libraries = []

        for library in grouper(f.readlines(), 2):
            libraries.append(Library(*library[0].split(), library[1].split()))

    return Input(n, t, m, books, libraries)


def iter_libraries(fname):
    with open(fname) as f:
        f.readline()
        f.readline()
        for library in grouper(f.readlines(), 2):
            yield Library(*library[0].split(), library[1].split())


if __name__ == "__main__":
    inp = read_input('input/a_example.txt')
    print(inp.n_books)
    print(inp.libraries[0].signup_time)
