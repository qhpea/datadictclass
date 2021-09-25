rules = {}

def rule(function):
    global rules
    name = function.__name__
    rules[name] = function
    return function