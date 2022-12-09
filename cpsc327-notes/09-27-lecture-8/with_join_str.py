import random, string

class StringJoiner(list):
    "Context manager to join a list of strings. Faster than repeated concatenation"
    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        # The arguments are usually None, but if an exception 
        # is raised inside the with, then its type, value, and
        # stack traceback are passed in
        self.result = "".join(self)         # join the list together into single string


# Using context manager:
with StringJoiner() as joiner:
    for i in range(15):
        joiner.append(random.choice(string.ascii_letters))  # treating joiner as list

print(joiner.result)


# Alternative without context manager:
joiner = ""
for i in range(15):
    joiner += random.choice(string.ascii_letters)
print(joiner)

# But this is very inefficient: the string joiner is immutable, so
# everytime we concatenate, we are actually creating new strings.