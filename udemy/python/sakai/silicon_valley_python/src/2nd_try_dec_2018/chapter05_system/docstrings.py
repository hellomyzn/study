def example_func(param1, param2):
    """
	This is document.
	    Args :
                param1 (strings): The first parameter.
                param2 (int): The second parameter.

		Returns:
                bool: The return value. True for success, False otherwise.
    """


    print(param1)
    print(param2)
    return True

print(example_func.__doc__)
