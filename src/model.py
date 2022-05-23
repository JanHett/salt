from typing import Callable, Optional

from .controller import AbstractController

# ------------------------------------------------------------------------------
# ABSTRACT MODEL
# ------------------------------------------------------------------------------

class AbstractModelEvent:
    """
    Events fired by models should extend this class and set the class attribute
    `_name`
    """
    def __init__(self, *args):
        self._args = args

    @property
    def name(self):
        return self._name

    @property
    def args(self):
        return self._args

class AbstractModel:
    """
    A model is a container for the current state of an entity. All models in
    Salt should erive from `AbstractModel` and should remain "dumb", i.e. they
    should be pure data management interfaces.

    Further, a model should not have knowledge about whether or not the
    programme is running in headless mode.
    """
    def __init__(self):
        self._event_handlers = {}
        self.controller: Optional[AbstractController] = None

    def serialize(self):
        raise NotImplementedError(
            "`AbstractModel.serialize()` must be implemented by child class")

    def deserialize(self):
        raise NotImplementedError(
            "`AbstractModel.deserialize()` must be implemented by child class")

    def register_event_handler(self, event: str, handler: Callable):
        """
        Register an event handler for an event with the name `event`
        """
        if event not in self._event_handlers:
            self._event_handlers[event] = set()

        self._event_handlers[event].add(handler)

    def remove_event_handler(self, event: str, handler: Callable):
        if event in self._event_handlers:
            self._event_handlers[event].remove(handler)

            if len(self._event_handlers[event]) == 0:
                del self._event_handlers[event]

    def _emit(self, event: AbstractModelEvent):
        """
        Emit `event` and call associated handlers with `event.args`
        """
        if event in self._event_handlers:
            for h in self._event_handlers[event.name]:
                h(*event.args)
