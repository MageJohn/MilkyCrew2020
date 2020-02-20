#!/usr/bin/env python3

from collections import namedtuple
from itertools import zip_longest

Library = namedtuple("Library", ['n_books', 'signup_time', 'throughput', 'books', 'index'])

Input = namedtuple("Input", ['n_books', 'n_libraries', 'n_days', 'books', 'libraries'])
f = open("csolution2.txt", "w")

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

        for i, library in enumerate(grouper(f.readlines(), 2)):
            libraries.append(Library(*library[0].split(), library[1].split(), i))

    return Input(n, t, m, books, libraries)


if __name__ == "__main__":
    inp = read_input('input/c_incunabula.txt')
    print(inp.n_books)
    lib = sorted(inp.libraries, key=lambda lib: lib.signup_time)
    f.write(str(len(lib))+ "\n")
    for i in range(int(len(lib))):
        f.write(str(i) + " " + lib[i].n_books +"\n")
        for x in range(int( lib[i].n_books)):
            f.write( lib[i].books[x]+" ")
        f.write("\n")
    print(inp.libraries[0].signup_time)
