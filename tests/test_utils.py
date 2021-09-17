import typing
from smartcast import is_dict, is_int, is_bool, is_str, is_float, is_union, is_list

def test_is_union():
    assert is_union(typing.Optional[int])
    assert is_union(typing.Union[int, str])

def test_is_list():
    assert is_list(typing.List)
    assert is_list(typing.List[int])
    assert is_list(list)

def test_is_dict():
    assert is_dict(typing.Dict)
    assert is_dict(typing.Dict[int, str])
    assert is_dict(dict)


def test_is_primitive():
    assert is_str(str)
    assert is_int(int)
    assert is_float(float)
    assert is_bool(bool)