from uuid import uuid4

from datetime import datetime

from .expression import Expression


def create_uuid(base = ""):
    return base + str(uuid4())


class DateObject(Expression):
    def __init__(self) -> None:
        super().__init__()

ABSOLUTE_TIME_EPOC = datetime(1900, 1, 1)
def absolute_time(date = None):
    now = datetime.now()

    if date is list:
        now = datetime(*date)
    
    if date is DateObject:
        pass

    elapsed = now - ABSOLUTE_TIME_EPOC
    return elapsed.total_seconds()