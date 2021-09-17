# Smart Cast

Recursively cast json to python `dataclasses`, `typing`, and `class`

# Features
Supports
- `List[TV]`
- `Dict[TK, TV]`
- `Optional[TV]`
- `Union`
- `dict`
- `list`
- `dataclass`
- `int`
- `str`
- `float`
- `boolean`
- `datetime`

# useage
```python
from smartcast import normal, cast
from typing import List
import json
value = [Hey(True)]
normal = normal(value)
jstr = json.dumps(normal)
jobj = json.loads(jstr)
revalue = cast(jobj, List[Hey])
```