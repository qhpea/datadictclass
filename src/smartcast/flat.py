def normal_flatten(value, rootname="value", output={}):
    """
    Flatten a normal/json object to a Dict[str, str]
    nested items have for
    
    """
    vt = type(value)
    if is_dict(vt):
        for k, v in value.items():
            assert "." not in k, "cannot flatten a key with a . in it"
            assert "[" not in k, "cannot flatten a key with a [ in it"
            assert "]" not in k, "cannot flatten a key with a ] in it"
            output = normal_flatten(v, f"{rootname}.{k}", output)
        return output
    if is_list(vt):
        for i, v in zip(itertools.count(), value):
            output = normal_flatten(v, f"{rootname}[{i}]", output)
        return output
    
    # TODO check if it's a primitive
    if isinstance(value, (str, int, float, bool, None)):
        output[rootname] = repr(value)
        return output
    raise TypeError(f"{rootname} is {type(value)} which is not allowed in a normal form object. Please use normal on the object first.")


from ast import literal_eval

import re

def parse_flat_path(path: str):
    regex = r"^([^\.\[\]]+)(\[[^\.\[\]]+\])*$"
    parts = path.split(".")
    path_parsed = []
    for part in parts:
        match = re.match(regex, part)
        assert match, f"failed to parse part {part}"
        for g in match.groups():
            gv = str(g)
            if gv.startswith("[") and gv.endswith("]"):
                path_parsed.append(int(gv[1:-1]))
            path_parsed.append(gv)
    return tuple(path_parsed)

def universal_get(on: Union[dict, list], key: Any, default = None):
    if on is dict:
        return on.get(key, default)
    if on is list:
        if key >= len(on):
            return default
        else:
            return on[key]
    raise TypeError("on must be either dict or list")

def deep_get(on: Union[dict, list], key: tuple, default = None):
    if on is None:
        return default
    
    key_head = key[0]
    key_rest = key[1:]

    if key_rest:
        return deep_get(universal_get(on, key_head), key_rest, default)
    else:
        return universal_get(on, key_head, default)


def deep_set(on: Union[dict, list], key: list, value: any, make_children = False):
    key_head = key[0]
    key_rest = key[1:]

    if on is None:
        if key_head is str:
            on = dict()
        if key_head is int:
            on = list()
        raise TypeError(f"invalid key {key_head}")

    if len(key) == 1:
        if on is dict:
            on[key_head] = value
        if on is list:
            assert key >= 0, "can't handle negative keys"
            if key >= len(on):
                new_len = key + 1
                on.extend([None] * (new_len - len(on)))
                assert len(on) == new_len
            on[key] = value
        return on
    else:
        on[key_head] = deep_set(on.get(key_head), key_rest, value)

def renest(stuff):
    for key, v in stuff:
        key_head = key[0]
        key_rest = key[1:]

def normal_roughen(flat_str: Dict[str, str]):
    "deflatten a dict flattend by normal_flatten into a normal form object"
    flat = {parse_flat_path(k) : literal_eval(v) for k,v in flat_str.items()}
    
    values = {}

    sorted_flat = sorted(flat, key = len)

    for key, value in sorted_flat:
        values[key] = value
        for i in range(len(key)-1):
            subkey = key[:i]
            last = subkey[i]
            if last is int:
                values[subkey] = list()
            elif last is dict:
                values[subkey] = dict()
            else:
                raise TypeError(f"did not expect {last} in path")