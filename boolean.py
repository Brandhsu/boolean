def uniform(n: int) -> int:
    """Generates a binary number with alternating ones and zeros in decimal format"""

    # input: 1, 2, 3, 4, 5, ...
    # output: 2, 5, 10, 21, 42, ...

    bits = 2
    for i in range(n - 1):
        bits *= 2
        if not i % 2:
            bits += 1

    return bits
