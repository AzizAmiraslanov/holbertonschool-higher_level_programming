#!/usr/bin/python3


def magic_string(x=[0]):
    x[0] = x[0] + 1
    return (("BestSchool" + ", ") * x[0])[:-2]