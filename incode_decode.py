def encode(my_string):
    binary_string = ''.join(format(ord(i), 'b').zfill(8) for i in my_string)
    return binary_string


def decode(binary_string: str):
    parts = [binary_string[i:i + 8] for i in range(0, len(binary_string), 8)]
    my_string = ''.join(chr(int(i, base=2)) for i in parts)
    return my_string


if __name__ == "__main__":
    x = encode("Rules of Optimization: "
               "Rule 1: Don't do it. "
               "Rule 2 (for experts only): Don't do it yet."
               " - Michael A. Jackson")
    print(x)
    y = decode(x)
    print(y)


