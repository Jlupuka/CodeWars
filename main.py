def dig_pow(n, p):
    n_ = list(str(n))
    count = 0
    for index, elem in enumerate(n_):
        count += int(elem) ** (p + index)
    count_ = count // n
    if count_ * n == count:
        return count_
    return -1


print(dig_pow(46288, 3))
print(dig_pow(92, 1))
dig_pow(46288, 5)
dig_pow(3456789, 1)
