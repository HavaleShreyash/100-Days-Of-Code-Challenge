def min_operations_to_equalize(n):
    """
    Calculate the minimum number of operations needed to make all elements of the array equal.

    Args:
    - n (int): The length of the array.

    Returns:
    - int: The minimum number of operations required.

    Explanation:
    This function computes the minimum operations required to make all elements of the array equal
    by calculating the average value of the array elements and determining the total operations
    needed to move each element to that average value.
    """
    # Calculate the average
    average = (2 * n - 1) // 2

    # Calculate the total operations needed to make each element equal to the average
    total_operations = 0
    for i in range(n):
        total_operations += abs((2 * i + 1) - average)

    return total_operations // 2  # Each operation affects two elements

if __name__ == '__main__':
    # Test cases
    print(min_operations_to_equalize(3))  # Output: 2
    print(min_operations_to_equalize(6))  # Output: 9
