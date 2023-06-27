l = ["Mon", "tue", "Wed", "The", "fri", "sat", "Sun"]


def change_words(words, func):
    for word in words:
        print(func(word))


sample_func = lambda word: word.capitalize()
change_words(l, sample_func)
