class CapitalIterable:
    def __init__(self, string):
        self.string = string

    def __iter__(self):             # makes CapitalIterable an iterable object
        return CapitalIterator(self.string)


class CapitalIterator:
    def __init__(self, string):
        # capitalize first letter of each word
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0

    def __next__(self):             # must implement __next__()
        if self.index == len(self.words):
            raise StopIteration()

        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):             # not required to implement __iter__(), but could be useful
        return self


a = CapitalIterable("hello world!")         # create iterable object
for x in a:                                 # for loop calls iter() on the object to create iterator
    print(x)