"""Todo store module"""

from .base import MemoryStore

from ..models.todo import TodoModel


class TodoStore(MemoryStore):
    model_class = TodoModel

    def create(self, **kwargs):
        kwargs.setdefault('status', False)
        return super(TodoStore, self).create(**kwargs)
