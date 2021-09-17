import typing

import enum
import dataclasses
from typing import Any, Dict, List, MutableMapping, Mapping, Type, Union, TypeVar, Sequence
from collections.abc import Iterable

TNormal = Union[Dict[str, "TNormal"], List["TNormal"], bool, int, float, str, None]

T = TypeVar('T') 
TC = Type[T]


def _many_cast(value: TNormal, typeofs:List[Type[T]], strict: bool = True) -> T:
    for typeof in typeofs:
        try:
            return cast(value, typeof)
        except Exception:
            pass
    raise Exception(f"{value} not any of valid types {typeofs}")

# flake8: noqa: C901
def cast(value: TNormal, typeof:Type[T], strict: bool = True) -> T:
    """
    Cast an normal (json) object to specfied type.
    """
    #log(f"cast {value} to {typeof}")

    if typeof is None and not value:
        return None

    if typeof is bool and isinstance(value, (str, bool)):
        return bool(value)
    if typeof is str and isinstance(value, (str)):
        return str(value)
    if typeof is int and isinstance(value, (str, int)):
        return int(value)
    if typeof is float and isinstance(value, (str, int, float)):
        return float(value)

    if typeof is typing.Union:
        raise Exception("typing.Union is not a valid type")

    # TODO handle datatype specificly
    if typeof is typing._SpecialForm and typeof._name == 'Union':
        possibe_types = typeof._subs_tree()[1:]
        return _many_cast(value, possibe_types, strict=strict)
    if hasattr(typing, "_UnionGenericAlias") and type(typeof) == getattr(typing, "_UnionGenericAlias"):
      
        possibe_types = list(typeof.__args__)
        return _many_cast(value, possibe_types, strict=strict)
        
    
    if type(typeof) == typing._GenericAlias:
        
        typename = typeof._name
        if typename is None:
            if typeof.__origin__ == typing.Union:
                typename = "Union"
        typeparams = typeof.__args__
        if typeof._name == "List":
            (list_type, ) = typeparams
            return [cast(v, list_type) for v in value]
        if typename == "Union":
            return _many_cast(value, typeparams, strict=strict)
        if typeof._name in ["Dict", "MutableMapping", "Mapping"]:
            (kt, vt) = typeparams
            return {cast(k, kt): cast(v, vt) for k,v in value.items()}
        raise Exception(f"unkown GenericAlias {typename}")

    if isinstance(value, typeof):
        return value

    if dataclasses.is_dataclass(typeof):
        
        as_dict = {field.name: cast(value[field.name], field.type)
                   for field in dataclasses.fields(typeof) if field.name in value}
        return typeof(**as_dict)

    if typeof is list:
        return [v for v in value]
    if typeof is dict:
        return {k: v for k, v in value.items()}
    if issubclass(typeof, enum.Enum):
        return typeof[value]
    if isinstance(value, dict):
        attrs = typing.get_type_hints(typeof)
        out = typeof()
        assert not strict or attrs.keys() >= value.keys(), "source has unkown key type"
        for attr, typeof in attrs.items():
            if attr in value:
                value = value[attr]
                setattr(out, attr, cast(typeof, value))
            elif not hasattr(out, attr):
                raise Exception(f"{typeof} missing required value for {attr}")
        return out
    # TODO dict
    # TODO list
    raise Exception(f"can't cast {value} to {typeof}")


def normal(value: Any) -> TNormal:
    """
    Convert a python object to normal form (so it can be json serlized)
    """
    if value is None:
        return None
    if isinstance(value, (str, int, bool)):
        return value
    if isinstance(value, dict):
        return {str(k): normal(v) for k, v in value.items()}
    if isinstance(value, list):
        return [normal(v) for v in value]
    if isinstance(value, enum.Enum):
        return value.name
    if dataclasses.is_dataclass(value):
        return normal(dataclasses.asdict(value))
    return normal(value.__dict__)

