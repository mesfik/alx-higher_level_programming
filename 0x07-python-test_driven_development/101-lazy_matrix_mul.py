#!/usr/bin/python3
"""
module for multiplies matrix using numpy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Function that multiplies 2 matrices by using the module NumPy
    Args: m_a: first matrix
          m_b: seccond matrix
    Return: result of the multiplication
    """

    return (np.matmul(m_a, m_b))
