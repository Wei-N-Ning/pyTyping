# source: https://www.programcreek.com/python/example/94066/typing.Iterator
# see also: pyFunctional/generators

from typing import Iterator, List

def get_options_to_test(self, tokens):  # type: (Iterator[str]) -> List[str]
        options_to_test = []
        token = next(tokens, None)

        while token:
            # "--" stops option parsing
            if token == "--":
                break

            if token[:1] and token[0] == "-":
                if token[:2] == "--" and len(token) > 2:
                    options_to_test.append(token[2:])
                elif len(token) == 2:
                    options_to_test.append(token[1:])

            token = next(tokens, None)

        return options_to_test 

