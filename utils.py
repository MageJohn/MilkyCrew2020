#!/usr/bin/env python3

from itertools import repeat
from collections import namedtuple
from os import listdir, path


INPUT_FILES = tuple(map(path.join, repeat('input/'), listdir('input/')))


# Named tuples give objects that can be accessed like attributes on an object.
# Therefore a Library object can be used like this:
# > lib = Library(10, 20, 3, [1, 2, 3, 4])
# > lib.n_books
# 10
# > lib.throughput
# 3

Library = namedtuple("Library", ['index', 'n_books', 'signup_time', 'throughput', 'books'])


Input = namedtuple("Input", ['n_books', 'n_libraries', 'n_days', 'books', 'libraries'])


# High level functions

def read_input(fname):
    with open(fname) as f:
        return Input(
            _read_input_lengths(f),
            _read_input_books(f),
            tuple(_read_input_libraries(f))
        )


def iter_libraries(fname):
    with open(fname) as f:
        # Skip the first two lines
        f.readline()
        f.readline()

        for l in _read_input_libraries(f):
            yield l


def book_to_libs(book_ids, libraries):
    books = {book: [] for book in book_ids}
    for lib in libraries:
        for book in lib.books:
            books[book].append(lib)
    return books

# Low level functions.
# Sam, don't worry how these work.

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip(*args)


def to_int_list(string):
    return list(map(int, string.split()))


def _read_input_lengths(fd):
    return to_int_list(fd.readline())


def _read_input_books(fd):
    return to_int_list(fd.readline())


def _read_input_libraries(fd):
    for i, library in enumerate(grouper(fd.readlines(), 2)):
        yield Library(i, *to_int_list(library[0]), to_int_list(library[1]))

if __name__ == "__main__":
    inp = read_input('input/a_example.txt')
    print(inp.n_books)
    print(inp.libraries[0].signup_time)
