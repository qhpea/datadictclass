def equal_to(y: _T) -> Callable[[_T], bool]:
    return y.__eq__


def greater_equal_than(y: _T) -> Callable[[_T], bool]:
    return y.__ge__
