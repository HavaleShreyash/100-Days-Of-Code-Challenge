def manipulate_string(operations):
    """
    Manipulates a string based on given operations.

    Parameters:
    operations (list): A list of string operations.

    Returns:
    str or None: Resulting string or None for operations '3' (print) or '4' (undo).
    """

    current_str = ''
    history = []

    for operation in operations:
        args = operation.split()

        if args[0] == '1':  # Append
            current_str += args[1]
            history.append(['1', len(args[1])])
        elif args[0] == '2':  # Delete
            deleted = current_str[-int(args[1]):]
            current_str = current_str[:-int(args[1])]
            history.append(['2', deleted])
        elif args[0] == '3':  # Print
            index = int(args[1]) - 1
            return current_str[index] if 0 <= index < len(current_str) else None
        elif args[0] == '4':  # Undo
            undo = history.pop()
            if undo[0] == '1':
                current_str = current_str[:-undo[1]]
            elif undo[0] == '2':
                current_str += undo[1]

if __name__ == "__main__":
    input_operations = input().strip().split(',')

    result = manipulate_string(input_operations)

    if result is not None:
        print(result)

# Sample Input and output:
# 1 abc,3 3,2 3,1 xy,3 2,4,4,3 1
# c