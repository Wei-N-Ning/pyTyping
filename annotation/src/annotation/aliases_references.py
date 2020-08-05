from typing import Text, Iterable, List, Tuple, ForwardRef

RowIt = Iterable[List[Text]]
Element = Tuple[Text, Text]

# references
# forward references is particularly useful when defining a method
# that returns an instance of the class;
Item_T = ForwardRef('Item')


class Item_T:
    def clone(self) -> Item_T:
        return Item_T()
