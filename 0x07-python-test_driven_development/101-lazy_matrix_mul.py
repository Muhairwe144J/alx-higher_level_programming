import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """ Multiplies two matrices using NumPy.

    Args:
        m_a (list of list): The first matrix.
        m_b (list of list): The second matrix.

    Returns:
        list of list: The resulting matrix.

    Raises:
        TypeError: If m_a or m_b is not a list of lists of integers or floats,
                   or if rows in m_a or m_b have different sizes.
        ValueError: If m_a or m_b is empty, or if multiplication is not possible.
    """
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists of integers/floats")
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists of integers/floats")
    if not m_a or not m_b:
        raise ValueError("m_a and m_b can't be empty")
    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.dot(m_a, m_b)
