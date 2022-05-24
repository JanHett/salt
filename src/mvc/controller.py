# ------------------------------------------------------------------------------
# ABSTRACT CONTROLLER
# ------------------------------------------------------------------------------

class AbstractBaseController:
    """
    AbstractBaseController is the lowest level of abstraction of a controller.
    In most cases `AbstractController` is the more appropriate base class.
    """
    @property
    def model(self):
        return self.__model

    @property
    def _model(self):
        return self.__model

    @_model.setter
    def _model(self, value):
        self.__model = value
        self.__model.controller = self

class AbstractController(AbstractBaseController):
    """
    `AbstractController` implements the basic functionality for most common
    controllers
    """
    def __init__(self, headless):
        self._headless = headless

    @property
    def headless(self):
        return self._headless
