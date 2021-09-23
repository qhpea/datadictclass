

from typing import Generic, TypeVar


def wrap_function(cls, func_name, *, auto_unbox = True, make_base = None, make_right = None, make_inline = None):
    func_name_base = f"__{func_name}__"
    func_name_inline = f"__i{func_name}__"
    func_name_right = f"__r{func_name}__"

    

    if make_base is None:
        pass

    def __add__(self, other, *args):
        unboxed_other = other.value if auto_unbox and other is Box else other
        if hasattr(self.value, func_name_base):
            try:
                r = getattr(self.value, func_name_base)(unboxed_other, *args)
                self.value = r
                return self
            except NotImplementedError as e:
                error = e
        if hasattr(unboxed_other, func_name_right):
            r = getattr(func_name_right)(self.value, *args)
            self.value = r
            return self
        elif error:
            raise error

    def __iadd__(self, other, *args):
        unboxed_other = other.value if auto_unbox and other is Box else other
        if hasattr(self.value, func_name_inline):
            return getattr(self.value, func_name_inline)(unboxed_other)

        error = None

        if hasattr(self.value, func_name_base):
            try:
                r = getattr(self.value, func_name_base)(unboxed_other)
                self.value = r
                return self
            except NotImplementedError as e:
                error = e
        if hasattr(unboxed_other, func_name_right):
            r = getattr(func_name_right)(self.value)
            self.value = r
            return self
        elif error:
            raise error
        self.value += other
        return self
    
    def __radd__(self, other, *args):
        unboxed_other = other.value if auto_unbox and other is Box else other

        
        if hasattr(unboxed_other, func_name_right):
            r = getattr(func_name_right)(self.value, *args)
            self.value = r
            return self
        elif error:
            raise error
        raise AttributeError(f"boxed {type(self.value)} does not have {func_name_right}")
    
    __add__.__name__ = func_name_base
    __radd__.__name__ = func_name_right
    __add__.__name__ = func_name_inline
    
    if make_base:
        setattr(cls, func_name_base, __add__)
    if make_right:
        
        setattr(cls, func_name_right, __radd__)
    if make_inline:
        setattr(cls, func_name_inline, __iadd__)

ValueType = TypeVar("ValueType")

class Box(Generic[ValueType]):
    def __init__(self, value: ValueType) -> None:
        self.value = value

    def __repr__(self) -> str:
        return self.value.__repr__()
    
    def __set

    def set(self, value):
        self.value = value
        return value

def set(on, value):
    if isinstance(on, Box):
        on.value = value
    if hasattr(hasattr(on, "set")):
        on.set(value)
    if hasattr

def setable(value):
    return isinstance(value, Box) or hasattr(value, "set")