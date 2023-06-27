class Call():
    def add_num_add_double(self, x, y):
        """Add adn double

        >>> c = Call()
        >>> c.add_num_add_double(1, 1)
        4

        """

        if type(x) is not int or type(y) is not int:
            raise ValueError

        result = x + y
        result *= 2
        return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
