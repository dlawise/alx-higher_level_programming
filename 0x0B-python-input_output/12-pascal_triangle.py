#!/usr/bin/python3
"""Defines a function that returns a list of lists of integers
    representing the Pascal's Triangle
"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n

    Returns a list of lists of integers representing the triangle
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tmp = triangles[-1]
        row = [1]
        for i in range(len(tmp) - 1):
            row.append(tmp[i] + tmp[i + 1])
        row.append(1)
        triangles.append(row)
    return triangles
