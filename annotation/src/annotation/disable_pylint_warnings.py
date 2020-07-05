
class F:
    def __getattr__(self, n):
        return n


if __name__ == '__main__':
    # the following line can piss pylint off
    print(F().iddqd) # pyline: disable=no-member

    # this can be useful when working with matplotlib


