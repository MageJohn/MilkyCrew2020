#!/usr/bin/env python3

from utils import *

import heapq

def solution(inp):
    days_left = inp.n_days
    solution = []


    while days_left > 0:
        libs = scores(inp.libraries, days_left)
        heapify(libs)
        solution.append(libs.pop(0))
        for lib in libs:
            i = 0
            while i < len(lib.books):
                if lib.books[i] in libs[A]solution[-1]




def scores(libs, days):
    return [(min(lib.throughput * (days - lib.signup_time), lib.n_books), lib.index) for lib in libs]


if __name__ = "__main__":
