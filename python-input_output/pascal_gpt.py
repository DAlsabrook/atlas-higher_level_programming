def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Args:
        n (int): Number of rows in the triangle.

    Returns:
        list: Pascal's Triangle represented as a list of lists.
    """
    triangle = []

    for row in range(n):
        if row == 0:
            triangle.append([1])
        else:
            prev_row = triangle[row - 1]
            new_row = [1] + [prev_row[i] + prev_row[i - 1] for i in range(1, row)] + [1]
            triangle.append(new_row)

    return triangle
