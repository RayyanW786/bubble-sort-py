from typing import TypeVar, Optional, MutableSequence, Protocol
from abc import abstractmethod


class SupportsComparison(Protocol):
    @abstractmethod
    def __lt__(self: 'T', other: 'T') -> bool: ...
    @abstractmethod
    def __gt__(self: 'T', other: 'T') -> bool: ...


T = TypeVar('T', bound=SupportsComparison)


class BubbleSort:
    def __init__(self) -> None:
        self.array: Optional[MutableSequence[T]] = None
        self.length: int = 0
        self.last_result: Optional[MutableSequence[T]] = None

    def sort(self, array: MutableSequence[T]) -> MutableSequence[T]:
        self.array: MutableSequence[T] = array
        self.length: int = len(array) - 1
        for x in range(self.length):
            for i in range(self.length):
                if self.array[i] > self.array[i + 1]:
                    self.array[i + 1], self.array[i] = self.array[i], self.array[i + 1]
            self.length -= 1
        self.last_result: MutableSequence[T] = array
        return self.array

    def last_result(self) -> Optional[MutableSequence[T]]:
        return self.last_result


bubble = BubbleSort()
print(bubble.sort([4, 99, 2, 50, 27, 7, 9, 100]))
