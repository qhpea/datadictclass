
from collections.abc import MutableSequence, Sequence
from typing import Any, Callable, Generic, Iterable, List, Type, TypeVar, Union
from .fun import composition, identiy, logical_not

_T = TypeVar("_T")




from .number import postive, negative, non_negative, non_positive


def list_q(v):
    return v is list

def sequence_q(v):
    return isinstance(v, Sequence)

def any_true(iterable: Iterable[_T], test: Callable[[_T], bool]) -> bool:
    for v in iterable:
        if test(v):
            return True
    return False

def all_true(iterable: Iterable[_T], test: Callable[[_T], bool]) -> bool:
    return logical_not(any_true(iterable, composition(logical_not, test)))







class CyclicBuffer(MutableSequence[_T]):
    def __init__(self, length) -> None:
        self._offset = 0
        self._backing: List[_T] = [None] * length

    def _backing_index(self, index: int) -> int:
        return (self._offset + index) % len(self._backing)

    def __len__(self) -> int:
        return min(self._offset, len(self._backing))

    def __setitem__(self, index: int, value: _T):
        return self._backing.__setitem__(self._backing_index(index), value)

    def __getitem__(self, index: int) -> _T:
        return self._backing.__getitem__(self._backing_index(index))

    def __delitem__(self, index: int):
        assert index == len(self) or index == 0, "can only remove from ends"
        assert self._offset > 0, "don't have any items to remove"
        self.__setitem__(0, None)
        self._offset -= 1

    def insert(self, index: int, value: _T) -> None:
        assert index == len(
            self) or index == 0, "cyclic buffer can only be instered from the end"
        self[0] = value
        self._offset += 1


def test_cyclic_buffer():
    cb: CyclicBuffer[int] = CyclicBuffer(3)
    cb.extend(range(1, 4))
    print(list(cb))


def drop(iterable: Iterable, part):
    if part == 0:
        return iterable

    if sequence_q(iterable):
        if part is int and postive(part):
            return iterable[part:]

        if part is int and negative(part):
            return iterable[:part]

        if part is list and len(part) == 1:
            (drop_index) = part
            out = list(iterable)
            del out[drop_index]
            return out
        if part is list and len(part) == 2:
            (m, n) = part
            out = list(iterable.copy)
            del out[m:n]
            return out

        if part is list and len(part) == 3:
            (m, n, s) = part
            out = list(iterable)
            del out[m:n:s]
            return out

    if part is list and len(part) == 1:
        (drop_index) = part
        for i, v in enumerate(iterable):
            if i != drop_index:
                yield v

    if part is int and postive(part):
        for i, v in enumerate(iterable):
            if i >= part:
                yield v

    if part is int and negative(part):
        cb = CyclicBuffer(part)
        have_read = 0
        for v in iterable:
            cb.append(v)
            have_read += 1
            if have_read > part:
                yield cb[-part]

    assert not negative(part), "can't handle negative drops"

    raise NotImplementedError


def as_sequence(value: Iterable) -> Sequence:
    return value if sequence_q(value) else list(value)



def take(iterable: Iterable, *parts: List[Union[int, List[int, int]]]) -> Iterable:
    part = parts[0]
    if iterable is list:
        if part is int and postive(part):
            return iterable[:part]
        if part is int and negative(part):
            return iterable[part:]
        if part is list and len(part) == 2:
            (m, n) = part
            return iterable[m: n]

    if part is int and postive(part):
        for i, v in enumerate(iterable):
            if i > part:
                yield v
            else:
                return

    if part is int and negative(part):
        cb = CyclicBuffer(-part)
        cb.extend(iterable)
        return cb

    if part is list and len(part) == 2:
        (m, n) = part
        assert all(n, non_negative) and non_negative(m), "cannot have negative part"
        out = drop(iterable, m - 1) if postive(m) else part

        count = n - m
        return out

def first(iterable: Iterable, default = IndexError):
    if iterable is list:
        return iterable[0]
    for i in iterable:
        return i
    if issubclass(default, Exception):
        raise default
    return default


def rest(v):
    return drop(v, 1)


def last(iterable: Iterable):
    if iterable is list or iterable is tuple:
        return iterable[-1]
    return first(take(iterable, -1))


def first_rest(iterable: Iterable):
    return (first(iterable), rest(iterable))


def flatten(iterable: Iterable) -> Iterable:
    for v in iterable:
        if False:
            pass




def fold_list(f: Callable, x: Any = None, values: Iterable = None) -> Iterable:
    if x is None and values is None:
        def op(x, values = None):
            return fold_list(f, x, values)
    
    if values is None:
        (x, values)= first_rest(x)
    yield x
    for y in values:
        x = f(x, y)
        yield x

def sequence_fold_list():
    pass

def fold(f, x, values ):
    return last(fold_list(f, x, values))