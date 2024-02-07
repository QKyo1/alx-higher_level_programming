#!/usr/bin/python3
"""
jokes on oyu
"""


def class_to_json(obj):
    """
    jokes on oyu
    """

    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
