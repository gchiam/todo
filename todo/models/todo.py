import collections

from .base import BaseModel

_TodoModel = collections.namedtuple(
    '_TodoModel',
    'id task status'
)


class TodoModel(BaseModel, _TodoModel):
    pass
