# see: https://www.python.org/dev/peps/pep-0484/#forward-references

# do:
class Tree:
    def __init__(self, left: 'Tree', right: 'Tree'):
        self.left = left
        self.right = right

