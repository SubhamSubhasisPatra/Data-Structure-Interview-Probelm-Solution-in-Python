"""
show_number(1, 3)
    show_number(2, 3)
        show_number(3, 3)
            show_number(4, 3)  // returns immediately without printing anything
        print(3)
    print(2)
print(1)

"""


from typing import Optional, TextIO


def show_number(c: int, i: int, buffer: Optional[TextIO] = None) -> None:
    """
    Recursively prints the numbers from c to i.

    Args:
    c (int): The starting number.
    i (int): The ending number.
    buffer (Optional[TextIO]): A file-like object to write the output to. If None, print to stdout.

    Returns:
    None
    """
    if c > i:
        return
    show_number(c + 1, i, buffer=buffer)
    output = str(c) + "\n"
    if buffer is not None:
        buffer.write(output)
    else:
        print(output, end='')


if __name__ == '__main__':
    show_number(1, 3)

