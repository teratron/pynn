# https://tproger.ru/articles/python-typing/
# https://docs-python.ru/standart-library/modul-typing-python/tip-annotatsii-typevar-modulja-typing/

# https://www.metatrader5.com/ru/metaeditor/help/development/python
# https://www.metatrader5.com/ru/terminal/help/algotrading/trade_robots_indicators#python
# https://www.mql5.com/ru/docs/integration/python_metatrader5
# https://dev-gang.ru/article/kak-podkluczitsja-k-metatrader--s-pomosczu-python-sswvfladkp/
# https://www.conorjohanlon.com/how-to-open-a-trade-in-mt5-with-python/


from typing import TypeVar, Generic, List

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        # Create an empty list with items of type T
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def empty(self) -> bool:
        return not self.items


def func(stack: Stack[int]) -> None:
    stack.push(11)
    stack.push(-2)


if __name__ == "__main__":
    s = Stack[int]()
    func(s)
    print(s.empty())
    print(s.items)
