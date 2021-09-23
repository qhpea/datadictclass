
from typing import Sequence
from smartcast.abstract import get_abstract_methods

class Forwarder:
    def __init__(self) -> None:
        pass

def forward(cls, to= "value", *fields: Sequence[str]):
    if not fields:
        fields = get_abstract_methods(cls)
    # setup soflink
    for field in fields:
        original = getattr(cls, field) if hasattr(cls, field) else None
        def wrapper(self, *args, **kwargs):
            return getattr(getattr(self, to), field)(*args, **kwargs)
        
        if original:
            print(original.__doc__)
            og_meta: dict = original.__dict__.copy()
            del og_meta["__isabstractmethod__"]
            wrapper.__dict__.update(og_meta)
            #wrapper.__annotations__ = original.__annotations__
            #wrapper.__doc__ = original.__doc__
        
        setattr(cls, field, wrapper)
    
    # create hardlink function for better performance
    def hardlink(self):
        for field in fields:
            setattr(cls, field, getattr(getattr(self, to), field))
    cls.hardlink = hardlink
    
    cls.__setup_
    return cls
